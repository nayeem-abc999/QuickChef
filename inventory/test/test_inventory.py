from django.test import TestCase
from django.contrib.auth.models import User
from inventory.models import Inventory, User_Info

class InventoryModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='nayeem', password='password')
        self.user_info = User_Info.objects.create(
            user=self.user,
            fName='Nayeem',
            lName='Anik',
            email='nayeem@example.com',
            phoneNumber='1234567890',
            dob='2000-01-01',
            total_waste=0
        )

    def test_create_inventory(self):
        inventory = Inventory.objects.create(userID=self.user_info)
        self.assertEqual(inventory.userID, self.user_info)

    def test_update_inventory(self):
        inventory = Inventory.objects.create(userID=self.user_info)
        new_user_info = User_Info.objects.create(
            user=self.user,
            fName='N',
            lName='Islam',
            email='n@example.com',
            phoneNumber='0987654321',
            dob='2000-01-01',
            total_waste=0
        )

        inventory.userID = new_user_info
        inventory.save()

        self.assertEqual(inventory.userID, new_user_info)

    def test_delete_inventory(self):
        inventory = Inventory.objects.create(userID=self.user_info)
        inventory_id = inventory.id

        inventory.delete()

        with self.assertRaises(Inventory.DoesNotExist):
            Inventory.objects.get(id=inventory_id)

    def test_query_inventory(self):
        inventory1 = Inventory.objects.create(userID=self.user_info)
        inventory2 = Inventory.objects.create(userID=self.user_info)

        inventories = Inventory.objects.all()
        self.assertEqual(len(inventories), 2)
        self.assertIn(inventory1, inventories)
        self.assertIn(inventory2, inventories)

    def test_query_inventory_empty(self):
        empty_inventories = Inventory.objects.all()
        self.assertEqual(len(empty_inventories), 0)
    
