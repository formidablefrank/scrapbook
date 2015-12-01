from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from webapp.views import index, create
from django.template.loader import render_to_string


class HomePageTest(TestCase):
	def test_root_url_resolves_to_index_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, index)


	def test_index_page_returns_correct_html(self):
		request = HttpRequest()
		response = index(request)
		expected_html = render_to_string('home/home.html')
		self.assertEqual(response.content.decode(), expected_html)


	def test_create_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['name'] = "Baby Bae First Twelve Months"
		request.POST['description'] = "Recording memorable events in Baby Bae\'s First 12 Months"
        request.POST['start_date'] = "11/18/2015"
        request.POST['frequency'] = "Monthly"
        request.POST['every'] = '3'
        request.POST['mode'] = "Days"
        request.POST['email'] = 'user@email.com'
		response = create(request)
		self.assertIn('Create Scrapbook', response.content.decode())
