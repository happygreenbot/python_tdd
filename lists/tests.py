from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest, HttpResponse

# Create your tests here.

# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

class HomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Using the Django test client to obtain the HttpResponse object from the url
        response = self.client.get('/')  

        # Using the assertTemplateUsed function to check if the expected template is being returned
        self.assertTemplateUsed(response, 'home.html')  

    def test_can_save_a_POST_request(self):
        # Send a post request to the '/' route and test the return HttpResponse object content
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
