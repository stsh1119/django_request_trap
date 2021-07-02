from django.test import TestCase
from django.urls import reverse, resolve

from .models import Request
from .services import find_requests_by_id
from .views import capture_request_view, display_request_data, HomePageView


class ViewsTests(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get(reverse('capture_request', kwargs={'request_id': 77}))

    def test_correct_absolute_url(self):
        r = Request.objects.first()
        self.assertEqual(r.get_absolute_url(), '/77/requests/')

    def test_capture_request_view(self):
        response = self.client.get(reverse('capture_request', kwargs={'request_id': 77}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Request captured, details are available at /77')
        self.assertTemplateUsed(response, 'request_captured.html')

    def test_display_request_data_view(self):
        response = self.client.get(reverse('display_requests', kwargs={'request_id': 77}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'request_details.html')

    def test_urls_resolve_correct_views(self):
        home = resolve('/')
        capture_view = resolve('/hello/')
        display_view = resolve('/hello/requests/')
        self.assertEqual(home.func.__name__, HomePageView.as_view().__name__)
        self.assertEqual(capture_view.func.__name__, capture_request_view.__name__)
        self.assertEqual(display_view.func.__name__, display_request_data.__name__)


class ServicesTests(TestCase):

    def test_save_request_data(self):
        self.client.get('/test/')
        request_in_db = Request.objects.first()

        self.assertEqual(request_in_db.request_id, 'test')
        self.assertNotEqual(request_in_db, 'test2')
        self.assertEqual(request_in_db.method, 'GET')
        self.assertNotEqual(request_in_db.method, 'POST')
        self.assertEqual(request_in_db.body, '')

    def test_find_requests_by_id(self):
        self.client.get('/request_1/')

        r = find_requests_by_id('request_1')
        self.assertEqual(r[0].request_id, 'request_1')
        self.assertEqual(r[0].method, 'GET')
