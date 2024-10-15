from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

#API data can be cached later to improve performance of app

#User Info
class User_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    fName = models.CharField(max_length=100,  null=True)
    lName = models.CharField(max_length=100,  null=True)
    email = models.EmailField(max_length=100,  null=True)
    phoneNumber = models.CharField(max_length=15,  null=True)
    dob = models.DateField( null=True)
    total_waste = models.DecimalField(max_digits = 4, decimal_places=2, default=0)
    

#User Preferences
class Preferences(models.Model):
    userID = models.ForeignKey(User_Info, on_delete=models.CASCADE, related_name='userIDD')
    vegan = models.BooleanField()
    vegetarian = models.BooleanField()
    halal = models.BooleanField()
    glutenFree = models.BooleanField()
    lactoseIntolerance = models.BooleanField()
    dairyFree = models.BooleanField()
    nutAllergy = models.BooleanField()
    Other = models.TextField()

#User Inventory
class Inventory(models.Model):
    userID = models.ForeignKey(User_Info, on_delete=models.CASCADE, related_name='userID')
    updated_at = models.DateTimeField(auto_now = True)

#Generic ingredients table. (Ex: banana, chicken)
#Can add nutrition information later as a way of caching API data
class IngredientsGeneric(models.Model):
    ingredientName = models.CharField(max_length=100)

#Specific ingredients table which links to user inventory.
class IngredientsSpecific(models.Model):
    inventoryID = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventoryID')
    ingredientID = models.ForeignKey(IngredientsGeneric, on_delete=models.CASCADE, related_name='ingredientID')
    dateOfPurchase = models.DateField(auto_now = True)
    expiryDate = models.DateField()
    quantity = models.DecimalField(max_digits = 5, decimal_places=2, default=0, validators=[MinValueValidator(0)])
