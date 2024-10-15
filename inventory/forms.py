from django import forms

class InventoryForm(forms.Form):
    food = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Name of Ingredient',}))
    weight = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'formfield', 'placeholder': 'Weight (grams)',}))
    expiry = forms.DateField(required=True,  widget=forms.DateInput(attrs={'class': 'formfield', 'placeholder': 'Expiry Date',}))