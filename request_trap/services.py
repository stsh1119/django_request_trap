from django.utils import timezone
from .models import Request
from django.core.handlers.wsgi import WSGIRequest
from typing import Iterable


def save_request_data(request: WSGIRequest, request_id: str) -> None:
    """Parses incoming request and saves its details to a db."""
    request = Request(request_id=request_id,
                      date=timezone.now(),
                      remote_ip=request.META.get('REMOTE_ADDR'),
                      method=request.method,
                      scheme=request.scheme,
                      query_string=request.META.get('QUERY_STRING'),
                      query_params=dict(request.GET),
                      cookies=request.COOKIES,
                      headers=request.headers,
                      body=request.body if request.body else '')

    request.save()


def find_requests_by_id(request_id: str) -> Iterable:
    """Finds all requests by given request_id and returns them sorted by creation date."""
    return Request.objects.filter(request_id=request_id).order_by('-date').all()
