from django.test import TestCase
from datetime import date
from django.core.exceptions import ValidationError
from inventory.models import IngredientsSpecific, Inventory, IngredientsGeneric, User_Info
from django.contrib.auth.models import User

class IngredientsSpecificModelTestCase(TestCase):
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
        self.inventory = Inventory.objects.create(userID=self.user_info)
        self.ingredients_generic = IngredientsGeneric.objects.create(ingredientName='Salt')

    def test_create_ingredients_specific(self):
        ingredients_specific = IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=10.5
        )
        self.assertEqual(ingredients_specific.inventoryID, self.inventory)
        self.assertEqual(ingredients_specific.ingredientID, self.ingredients_generic)
        self.assertEqual(ingredients_specific.expiryDate, date.today())
        self.assertEqual(ingredients_specific.quantity, 10.5)

    
    def test_expiry_date_in_past(self):
        expiry_date = date.today().replace(year=date.today().year - 1)
        ingredients_specific = IngredientsSpecific(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=expiry_date,
            quantity=5.0
        )
    
        self.assertNotEqual(ingredients_specific.expiryDate, date.today())

    


    def test_quantity_zero(self):
        ingredients_specific = IngredientsSpecific(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=0
        )
        self.assertNotEqual(ingredients_specific.quantity , 5)

    def test_negative_quantity(self):
        ingredients_specific = IngredientsSpecific(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=-5.0
        )
        with self.assertRaises(ValidationError):
            ingredients_specific.full_clean()


    def test_query_ingredients_specific_by_inventory(self):
        ingredients_specific1 = IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=5.0
        )
        ingredients_specific2 = IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=3.0
        )
        ingredients = IngredientsSpecific.objects.filter(inventoryID=self.inventory)
        self.assertEqual(len(ingredients), 2)
        self.assertIn(ingredients_specific1, ingredients)
        self.assertIn(ingredients_specific2, ingredients)


    def test_query_ingredients_specific_by_ingredient(self):
        IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=5.0
        )
        ingredients_specific2 = IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=3.0
        )
        ingredients = IngredientsSpecific.objects.filter(ingredientID=self.ingredients_generic)
        self.assertEqual(len(ingredients), 2)
        self.assertIn(ingredients_specific2, ingredients)

    def test_query_ingredients_specific_expiring_today(self):
        IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=5.0
        )
        IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=3.0
        )
        expiring_today = IngredientsSpecific.objects.filter(expiryDate=date.today())
        self.assertEqual(len(expiring_today), 2)

    def test_query_ingredients_specific_expired(self):
        IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today().replace(year=date.today().year - 1),
            quantity=5.0
        )
        expired = IngredientsSpecific.objects.filter(expiryDate__lt=date.today())
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0].inventoryID, self.inventory)

    def test_query_ingredients_specific_quantity_gt_5(self):
        IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=10.0
        )
        IngredientsSpecific.objects.create(
            inventoryID=self.inventory,
            ingredientID=self.ingredients_generic,
            expiryDate=date.today(),
            quantity=3.0
        )
        quantity_gt_5 = IngredientsSpecific.objects.filter(quantity__gt=5.0)
        self.assertEqual(len(quantity_gt_5), 1)
        self.assertEqual(quantity_gt_5[0].inventoryID, self.inventory)

