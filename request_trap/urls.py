from django.urls import path
from .views import HomePageView, capture_request_view, display_request_data

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('<str:request_id>/', capture_request_view, name='capture_request'),
    path('<str:request_id>/requests/', display_request_data, name='display_requests'),
]
