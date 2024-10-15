from django.test import TestCase
from django.contrib.auth.models import User
from inventory.models import User_Info, Preferences


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='john', password='password')
        self.user_info = User_Info.objects.create(
            user=self.user,
            fName='Islam',
            lName='Nayeemul',
            email='n@example.com',
            phoneNumber='12345678910',
            dob='2000-01-01',
            total_waste=0
        )

    
    def test_create_preferences(self):
        preferences = Preferences.objects.create(
            userID=self.user_info,
            vegan=True,
            vegetarian=False,
            halal=False,
            glutenFree=True,
            lactoseIntolerance=False,
            dairyFree=True,
            nutAllergy=False,
            Other='No specific preferences'
        )
        self.assertEqual(preferences.userID.fName, 'Islam')
        self.assertTrue(preferences.vegan)
        self.assertFalse(preferences.vegetarian)
        self.assertFalse(preferences.halal)
        self.assertTrue(preferences.glutenFree)
        self.assertFalse(preferences.lactoseIntolerance)
        self.assertTrue(preferences.dairyFree)
        self.assertFalse(preferences.nutAllergy)
        self.assertEqual(preferences.Other, 'No specific preferences')

    def test_update_preferences(self):
        preferences = Preferences.objects.create(
            userID=self.user_info,
            vegan=True,
            vegetarian=False,
            halal=False,
            glutenFree=True,
            lactoseIntolerance=False,
            dairyFree=True,
            nutAllergy=False,
            Other='No specific preferences'
        )
        preferences.glutenFree = False
        preferences.save()
        self.assertFalse(preferences.halal)

    def test_query_user_info(self):
        user_info1 = User_Info.objects.create(
            user=self.user,
            fName='James',
            lName='Wood',
            email='james@example.com',
            phoneNumber='1234567890',
            dob='2000-01-01',
            total_waste=10
        )
        user_infos = User_Info.objects.filter(total_waste__gt=0)
        self.assertEqual(len(user_infos), 1)
        self.assertEqual(user_infos[0].fName, 'James')
        self.assertEqual(user_infos[0].lName, 'Wood')
        self.assertEqual(user_infos[0].total_waste, 10)

    def test_query_preferences(self):
        preferences1 = Preferences.objects.create(
            userID=self.user_info,
            vegan=True,
            vegetarian=False,
            halal=False,
            glutenFree=True,
            lactoseIntolerance=False,
            dairyFree=True,
            nutAllergy=False,
            Other='No specific preferences'
        )
        preferences2 = Preferences.objects.create(
            userID=self.user_info,
            vegan=False,
            vegetarian=True,
            halal=True,
            glutenFree=False,
            lactoseIntolerance=True,
            dairyFree=False,
            nutAllergy=True,
            Other='Specific preferences good food'
        )
        preferences = Preferences.objects.filter(userID=self.user_info)
        self.assertEqual(len(preferences), 2)
        self.assertEqual(preferences[0].Other, 'No specific preferences')
        self.assertEqual(preferences[1].Other, 'Specific preferences good food')

    def test_query_preferences_multiple_conditions(self):
        Preferences.objects.create(
            userID=self.user_info,
            vegan=True,
            vegetarian=False,
            halal=False,
            glutenFree=True,
            lactoseIntolerance=False,
            dairyFree=True,
            nutAllergy=False,
            Other='No specific preferences'
        )
        Preferences.objects.create(
            userID=self.user_info,
            vegan=False,
            vegetarian=True,
            halal=True,
            glutenFree=False,
            lactoseIntolerance=True,
            dairyFree=False,
            nutAllergy=True,
            Other='Specific preferences'
        )

        preferences = Preferences.objects.filter(vegan=True, glutenFree=True)
        self.assertEqual(len(preferences), 1)
        self.assertEqual(preferences[0].Other, 'No specific preferences')

    def test_delete_user_info(self):
        preferences = Preferences.objects.create(
            userID=self.user_info,
            vegan=True,
            vegetarian=False,
            halal=False,
            glutenFree=True,
            lactoseIntolerance=False,
            dairyFree=True,
            nutAllergy=False,
            Other='No specific preferences'
        )
        user_info_id = self.user_info.id
        preferences_id = preferences.id

        self.user_info.delete()

        with self.assertRaises(User_Info.DoesNotExist):
            User_Info.objects.get(id=user_info_id)
    
        with self.assertRaises(Preferences.DoesNotExist):
            Preferences.objects.get(id=preferences_id)
