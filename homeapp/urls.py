from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/issue', views.issue, name='issue'),
    path('/mission', views.mission, name='mission'),
    path('/team', views.team, name='team'),
    path('/signup', views.RegisterUser.as_view(), name='signup'),
    path('user/update', views.user_update, name='user_update'),
    path('user/details', views.user_details, name='user_details'),
    path('user/preferences', views.user_preferences, name='user_preferences'),
    path('user/preferences/update', views.user_preferences_update, name='user_preferences_update'),

]