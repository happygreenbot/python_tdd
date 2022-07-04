from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest, HttpResponse
from lists.models import Item

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

        # Counting number of items in table and and asserting
        self.assertEqual(Item.objects.count(), 1)  
        new_item = Item.objects.first()  
        self.assertEqual(new_item.text, 'A new list item')  

    def test_redirect_after_a_POST_request(self):
        # Send a post request to the '/' route and test the return HttpResponse object content
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    
class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
