from django.test import TestCase, Client
from django.contrib.auth.models import User
from inventory.models import Inventory, User_Info
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_my_kitchen_page(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/inventory.html')
        self.assertContains(response, '<title>My Kitchen</title>')
        self.assertContains(response, '<h3>My Kitchen</h3>')
        self.assertContains(response, '<button class="toggle-btn" id="inventory-button">Inventory</button>')
        self.assertContains(response, '<button class="toggle-btn" id="to-buy-button">To Buy</button>')
        self.assertContains(response, '<button class="toggle-btn" id="thrown-away-button">Thrown Away</button>')
        self.assertContains(response, '<form method="POST" enctype="multipart/form-data" onsubmit="return validateForm()" class="kitchen-form">')
        self.assertContains(response, '<input type="submit" id="submit" value="Submit" class="btn btn-primary submit-button">')
        self.assertContains(response, '<table id="kitchen-table" class="table">')

        # Check the table headers
        self.assertContains(response, '<th>Name</th>')
        self.assertContains(response, '<th>Weight (g)</th>')
        self.assertContains(response, '<th>Expiry Date</th>')
        self.assertContains(response, '<th>Action</th>')

        # Check the empty table message
        self.assertContains(response, 'Inventory table is currently empty, start adding Food!')




