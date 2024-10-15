from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from inventory.models import User_Info
from django.core.exceptions import ValidationError
from decimal import Decimal

class User_InfoTestCase(TestCase):
    def setUp(self):
        # Create a User object
        self.user = User.objects.create_user(username='nayeem', password='password')

    def test_user_info_creation(self):
        # Create a User_Info object
        user_info = User_Info.objects.create(
            user=self.user,
            fName='Nayeem',
            lName='Anik',
            email='nayeem@example.com',
            phoneNumber='1234567890',
            dob=date(2001, 1, 1),
            total_waste=0
        )
        # Assert that the User_Info object is created successfully
        self.assertIsNotNone(user_info)
        self.assertEqual(user_info.fName, 'Nayeem')
        self.assertEqual(user_info.lName, 'Anik')
        self.assertEqual(user_info.email, 'nayeem@example.com')
        self.assertEqual(user_info.phoneNumber, '1234567890')
        self.assertEqual(user_info.dob, date(2001, 1, 1))
        self.assertEqual(user_info.total_waste, 0)
    
    def test_user_info_user_null(self):
        user_info = User_Info.objects.create(fName='Jane', lName='Smith', email='jane.smith@example.com')
        self.assertIsNone(user_info.user)
    
    def test_user_info_email_valid(self):
        user_info = User_Info.objects.create(email='test@example.com')
        self.assertEqual(user_info.email, 'test@example.com')

    def test_user_info_phone_number_length(self):
        user_info = User_Info.objects.create(phoneNumber='12345678911')
        self.assertEqual(len(user_info.phoneNumber), 11)

    def test_user_info_total_waste_decimal_places(self):
        user_info = User_Info.objects.create(total_waste=Decimal('5.12'))
        self.assertEqual(user_info.total_waste, Decimal('5.12'))
    
    def test_user_info_update(self):
        # Create a User_Info object
        user_info = User_Info.objects.create(
            user=self.user,
            fName='Nayeem',
            lName='Anik',
            email='nayeem@example.com',
            phoneNumber='1234567890',
            dob=date(2001, 1, 1),
            total_waste=0
        )
        # Update the User_Info object
        user_info.fName = 'Updated Name'
        user_info.lName = 'Updated Last Name'
        user_info.save()

        # Retrieve the updated User_Info object from the database
        updated_user_info = User_Info.objects.get(id=user_info.id)

        # Assert that the User_Info object is updated successfully
        self.assertEqual(updated_user_info.fName, 'Updated Name')
        self.assertEqual(updated_user_info.lName, 'Updated Last Name')
    
    def test_user_info_total_waste_default_value(self):
        # Create a User_Info object without providing the total_waste value
        user_info = User_Info.objects.create(
            user=self.user,
            fName='Nayeem',
            lName='Anik',
            email='nayeem@example.com',
            phoneNumber='1234567890',
            dob=date(2001, 1, 1)
        )

        # Assert that the total_waste value is set to the default value (0)
        self.assertEqual(user_info.total_waste, 0)
    
    def test_user_info_deletion(self):
        # Create a User_Info object
        user_info = User_Info.objects.create(
            user=self.user,
            fName='Nayeem',
            lName='Anik',
            email='nayeem@example.com',
            phoneNumber='1234567890',
            dob=date(2001, 1, 1),
            total_waste=0
        )
        # Delete the User_Info object
        user_info.delete()

        # Try to retrieve the deleted User_Info object from the database
        with self.assertRaises(User_Info.DoesNotExist):
            User_Info.objects.get(id=user_info.id)
