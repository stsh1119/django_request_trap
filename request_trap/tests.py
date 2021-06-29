from django.test import TestCase
from django.utils import timezone
from django.urls import reverse, resolve
from .models import Request
from .services import save_request_data, find_requests_by_id
from .views import capture_request_view, display_request_data, HomePageView


class ServicesTests(TestCase):

    def setUp(self) -> None:
        request = Request(request_id='Unit_test',
                          date=timezone.now(),
                          remote_ip='127.0.0.1',
                          method='GET',
                          scheme='http',
                          query_string='hello=1&r=2',
                          query_params={'hello': ['1'], 'r': ['2']},
                          cookies='test_cookie',
                          headers='some_headers',
                          body='')
        request.save()

    def test_find_requests_by_id(self):
        r = find_requests_by_id(request_id='Unit_test')
        self.assertEqual(r[0].request_id, 'Unit_test')
        self.assertEqual(r[0].method, 'GET')

    def test_save_request_data(self):
        pass

    def test_capture_request_view(self):
        response = self.client.get(reverse('capture_request', kwargs={'request_id': 77}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'request_captured.html')

    def test_urls_resolve_correct_views(self):
        home = resolve('/')
        capture_view = resolve('/hello/')
        display_view = resolve('/hello/requests/')
        self.assertEqual(home.func.__name__, HomePageView.as_view().__name__)
        self.assertEqual(capture_view.func.__name__, capture_request_view.__name__)
        self.assertEqual(display_view.func.__name__, display_request_data.__name__)
