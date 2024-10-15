from django.test import TestCase
from inventory.models import IngredientsGeneric

class IngredientsGenericModelTestCase(TestCase):
    def test_create_ingredients_generic(self):
        ingredient = IngredientsGeneric.objects.create(ingredientName='Salt')
        self.assertEqual(ingredient.ingredientName, 'Salt')

    def test_update_ingredients_generic(self):
        ingredient = IngredientsGeneric.objects.create(ingredientName='Salt')
        ingredient.ingredientName = 'Sugar'
        ingredient.save()
        self.assertEqual(ingredient.ingredientName, 'Sugar')

    def test_delete_ingredients_generic(self):
        ingredient = IngredientsGeneric.objects.create(ingredientName='Salt')
        ingredient_id = ingredient.id

        ingredient.delete()

        with self.assertRaises(IngredientsGeneric.DoesNotExist):
            IngredientsGeneric.objects.get(id=ingredient_id)
    def test_query_ingredients_generic(self):
        ingredient1 = IngredientsGeneric.objects.create(ingredientName='Salt')
        ingredient2 = IngredientsGeneric.objects.create(ingredientName='Sugar')

        ingredients = IngredientsGeneric.objects.all()
        self.assertEqual(len(ingredients), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients)

    def test_query_ingredients_generic_by_name(self):
        IngredientsGeneric.objects.create(ingredientName='Salt')
        IngredientsGeneric.objects.create(ingredientName='Sugar')

        ingredient = IngredientsGeneric.objects.get(ingredientName='Salt')
        self.assertEqual(ingredient.ingredientName, 'Salt')