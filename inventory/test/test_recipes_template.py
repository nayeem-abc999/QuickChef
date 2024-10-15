from django.test import TestCase, Client
from django.contrib.auth.models import User
from inventory.models import Inventory, User_Info, IngredientsGeneric
from django.urls import reverse

class RecipesNutritionTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_css_stylesheets(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, 'css/navbar.css')
        self.assertContains(response, 'css/recipes_nutrition.css')

    def test_recipes_nutrition_page(self):
        response = self.client.get(reverse("recipes"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "inventory/recipes.html")

    def test_page_contains_heading(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, "<h1 class=\"my-3 page-title text-center\">Recipes & Nutrition</h1>")

    def test_nutritional_info_section_displayed(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, "<div id=\"nutritional-info\">")

    def test_suggested_recipes_section_hidden(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, '<div id="suggested-recipes" class="d-none">')

    def test_nutritional_info_section_title(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, "<h2 class=\"mb-3 section-title\">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspNutritional Information on Current Inventory</h2>")

    def test_toggle_button_present(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, '<button class="btn toggle-btn active mx-0" id="nutritional-info-btn" style="background-color: #02a284; color: white;">Nutritional Info & Calories</button>')

