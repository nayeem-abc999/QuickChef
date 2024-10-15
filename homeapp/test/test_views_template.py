from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homeapp/index.html')

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homeapp/signup.html')

    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_navbar_in_home_page(self):
        navbar = 'css/navbar.css'
        self.assertContains(self.response, navbar)

    def test_image_in_home_page(self):
        image = 'images/reduce-waste.gif'
        self.assertContains(self.response, image)

    def test_footer_in_home_page(self):
        footer = '<div class="footer-container">'
        self.assertContains(self.response, footer)

    def test_about_section_in_home_page(self):
        section_text = 'About Quick Chef'
        self.assertContains(self.response, section_text)

    def test_get_started_button_in_home_page(self):
        button_text = 'Get Started'
        self.assertContains(self.response, button_text)
        
    def test_menu_section(self):
        menu_section_title = "What's on the menu?"
        meal_names = ['Vegetable steak with salad', 'Courgette cake', 'Indian chicken curry', 'Apple banana cream']
        for name in meal_names:
            self.assertContains(self.response, name)
        self.assertContains(self.response, menu_section_title)

    def test_footer_links_in_home_page(self):
        links_text = ['Privacy', 'Terms & Conditions', 'Cookie Policy']
        for link in links_text:
            self.assertContains(self.response, link)
    



