from django.test import TestCase, Client
from django.contrib.auth.models import User
from inventory.models import Inventory, User_Info
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)


    def test_impact_page(self):
        response = self.client.get(reverse('impact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/impact.html')
        self.assertContains(response, '<title>User\'s positive impact</title>')
        self.assertContains(response, '<h2 style="font-weight: bold;">User\'s positive impact</h2>')
        self.assertContains(response, '<h3 class="title2">Your food waste summary</h3>')
        self.assertContains(response, '<h3 class="title2">Weekly food waste cost</h3>')

    def test_summary_field(self):
        response = self.client.get(reverse('impact'))
        self.assertContains(response, '<div class="container active1" id="summary-field">')
        self.assertContains(response, '<div class="summary" id="type-of-save">')
        self.assertContains(response, '<h2 style="font-weight: bold;">User\'s positive impact</h2>')
        self.assertContains(response, '<div id="type-1st">')
        self.assertContains(response, '<div id="type-2nd">')        

    def test_time_of_use_field(self):
        response = self.client.get(reverse('impact'))
        self.assertContains(response, '<div class="summary" id="time-of-use">')
        self.assertContains(response, '<p class="goal-text" id="add-goal-title">Add your motivation for using QuickChef</p>')
        self.assertContains(response, '<p class="goal-text">You\'ve been using Quick Chef for <strong>0 weeks</strong></p>')
        self.assertContains(response, '<div class="progress-container " style="width: 80%;display: inline-block;">')
        self.assertContains(response, '<p class="goal-text"><strong style="color: #02a284">8 weeks</strong> to go</p>')

    def test_food_waste_summary(self):
        response = self.client.get(reverse('impact'))
        self.assertContains(response, '<h3 class="title2">Your food waste summary</h3>')
        self.assertContains(response, '<button class="btn" id="thisweek-btn" onclick="activate3()"><div id="thisweek-child-text">This week</div></button>')
        self.assertContains(response, '<button class="btn" id="lastweek-btn" onclick="activate4()"><div id="lastweek-child-text">Last week</div></button>')
        self.assertContains(response, '<div class="container active3" id="thisweek-text">')
        self.assertContains(response, '<div class="container" id="lastweek-text">')

    def test_weekly_food_waste_cost(self):
        response = self.client.get(reverse('impact'))
        self.assertContains(response, '<h3 class="title2">Weekly food waste cost</h3>')
        self.assertContains(response, '<div class="chart-container">')
        self.assertContains(response, '<canvas id="line-chart"></canvas>')