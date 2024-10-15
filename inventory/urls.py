from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('recipes', views.recipes, name='recipes'),
    path('impact', views.impact, name='impact'),
]