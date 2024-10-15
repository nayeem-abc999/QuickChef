from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from inventory.models import User_Info, Preferences

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "email")



class UserForm(forms.ModelForm):
    class Meta:
        model = User_Info
        labels ={'fName': 'First Name', 'lName': 'Last Name', 'email' : "E-mail", 'phoneNumber' :'Phone Number', 'dob' : 'Date of Birth' }
        fields = ['fName', 'lName', 'email', 'phoneNumber', 'dob']


class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Preferences
        labels = {'vegan': 'Vegan', 'vegetarian' : "Vegetarian", 'halal' : 'Halal', 'glutenFree': 'Gluten Free', 
                  'lactoseIntolerance': 'Lactose Intolerance', 'dairyFree': 'Dairy Free', 'nutAllergy': 'Nut Allergy', 'Other': 'Other'}
        fields = ('vegan', 'vegetarian', 'halal', 'glutenFree', 'lactoseIntolerance', 'dairyFree', 'nutAllergy', 'Other')