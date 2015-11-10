from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from webapp.views import index
from django.template.loader import render_to_string


class HomePageTest(TestCase):
	def test_root_url_resolves_to_index_page_view(self):
		found = resolve('/') #
		self.assertEqual(found.func, index) #

	def test_index_page_returns_correct_html(self):
		request = HttpRequest()
		response = index(request)
		expected_html = render_to_string('webapp/home.html')
		self.assertEqual(response.content.decode(), expected_html)
