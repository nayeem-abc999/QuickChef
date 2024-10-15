from django.urls import path
from . import views

urlpatterns = [
    path('', views.leaderboard, name = 'leaderboard'),
     path('leaderboard_data/', views.leaderboard_data, name='leaderboard_data'),

]