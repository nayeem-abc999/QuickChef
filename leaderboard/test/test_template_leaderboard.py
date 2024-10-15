from django.test import TestCase
from leaderboard.models import Leaderboard, User_Info
from django.urls import reverse

class LeaderboardTests(TestCase):
    def setUp(self):
        self.user_info = User_Info.objects.create(
            fName='Islam',
            lName='nayeemul',
            email='n@example.com',
            phoneNumber='1234567890',
            dob='2000-01-01',
            total_waste=0
        )
        self.user_info_2 = User_Info.objects.create(
            fName='James',
            lName='Watt',
            email='james@example.com',
            phoneNumber='1234567890',
            dob='2000-01-01',
            total_waste=0
        )

