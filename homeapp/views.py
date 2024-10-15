from django.shortcuts import render, redirect 
from .forms import SignUpForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from inventory.models import User_Info
from django.contrib import messages
from .forms import *
# Create your views here.
def home(request):
    context = {}
    return render(request, 'homeapp/index.html', context)

def issue(request):
    context = {}
    return render(request, 'homeapp/issue.html', context)

def mission(request):
    context = {}
    return render(request, 'homeapp/mission.html', context)

def team(request):
    context = {}
    return render(request, 'homeapp/team.html', context)


class RegisterUser(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'homeapp/signup.html'
    success_url = reverse_lazy('login')


@login_required
def user_update(request):    
    if request.method == 'POST':
        
        form = UserForm(request.POST)
        if form.is_valid():
            User_Info.objects.filter(user=request.user).delete()
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            # Redirect to a success page or do something else
            return redirect('user_details')
    else:
        form = UserForm()
    return render(request, 'homeapp/user_form.html', {'form': form})


@login_required
def user_details(request):
    try:
        user_info = User_Info.objects.get(user=request.user)
    except User_Info.DoesNotExist:
        messages.info(request, 'Please update your details first.')
        return redirect('user_update')
    user_info = User_Info.objects.get(user=request.user)
    return render(request, 'homeapp/user_details.html', {'user_info': user_info})

@login_required
def user_preferences(request):
    try:
        preferences = Preferences.objects.get(userID__user=request.user)
    except Preferences.DoesNotExist:
        return redirect(user_preferences_update)
    
    preferences = Preferences.objects.get(userID__user=request.user)
    return render(request, 'homeapp/user_preferences.html', {'preferences': preferences})


@login_required
def user_preferences_update(request):
    try:
        preferences = Preferences.objects.get(userID__user=request.user)
    except Preferences.DoesNotExist:
        preferences = None

    if request.method == 'POST':
        form = PreferencesForm(request.POST, instance=preferences)
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.userID = User_Info.objects.get(user=request.user)
            preferences.save()
            # Redirect to a success page or do something else
            return redirect('user_preferences')
    else:
        form = PreferencesForm(instance=preferences)

    return render(request, 'homeapp/preferences_form.html', {'form': form})
