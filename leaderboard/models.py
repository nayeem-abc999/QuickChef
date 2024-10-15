from django.db import models
from inventory.models import User_Info
# Create your models here.
class Leaderboard(models.Model):
    userID = models.ForeignKey(User_Info, on_delete=models.CASCADE, related_name='leaderboardID',primary_key=True)
    score = models.IntegerField(default=0)
   