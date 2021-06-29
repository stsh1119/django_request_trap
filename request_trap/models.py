from djongo import models
from django.urls import reverse


class Request(models.Model):
    """Model, representing HTTP request with its main parts."""
    request_id = models.CharField(max_length=100)
    date = models.DateTimeField()
    remote_ip = models.CharField(max_length=20)
    method = models.CharField(max_length=10)
    scheme = models.CharField(max_length=5)
    query_string = models.CharField(max_length=100)
    query_params = models.CharField(max_length=100)
    cookies = models.TextField()
    headers = models.TextField()
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('display_requests', args=[str(self.request_id)])

    def __repr__(self):
        return self.request_id
