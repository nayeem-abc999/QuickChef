from django.test import TestCase
from leaderboard.models import Leaderboard, User_Info

class LeaderboardModelTestCase(TestCase):
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

    def test_create_leaderboard_entry(self):
        leaderboard = Leaderboard.objects.create(
            userID=self.user_info,
            score=100
        )
        self.assertEqual(leaderboard.userID, self.user_info)
        self.assertEqual(leaderboard.score, 100)

    def test_default_score(self):
        leaderboard = Leaderboard.objects.create(
            userID=self.user_info
        )
        self.assertEqual(leaderboard.score, 0)


    def test_query_leaderboard_entries(self):
        leaderboard1 = Leaderboard.objects.create(
            userID=self.user_info,
            score=150
        )
        leaderboard2 = Leaderboard.objects.create(
            userID=self.user_info_2,
            score=200
        )
        leaderboard_entries = Leaderboard.objects.all()
        self.assertEqual(len(leaderboard_entries), 2)
        self.assertIn(leaderboard1, leaderboard_entries)
        self.assertIn(leaderboard2, leaderboard_entries)
