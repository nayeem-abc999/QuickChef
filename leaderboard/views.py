from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Leaderboard


# Create your views here.
@login_required
def leaderboard(request):
    context = {}
    context["leaderboard"] = Leaderboard.objects.order_by('-score')
    context["table"] = []
    scores = Leaderboard.objects.order_by('-score')
    scores2 = Leaderboard.objects.order_by('-score').values_list('score', flat=True)
    for i in range(len(scores)):
        username = User.objects.get(id=scores[i].userID.id).username
        context["table"].append([username,scores2[i]])
    return render(request, "leaderboard/leaderboard.html", context)

from django.http import JsonResponse

@login_required
def leaderboard_data(request):
    table = []
    scores = Leaderboard.objects.order_by('-score')
    scores2 = Leaderboard.objects.order_by('-score').values_list('score', flat=True)
    for i in range(len(scores)):
        username = User.objects.get(id=scores[i].userID.id).username
        table.append([username, scores2[i]])
    
    # return the leaderboard data as JSON
    return JsonResponse(table, safe=False)
