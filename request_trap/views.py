from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .services import save_request_data, find_requests_by_id


class HomePageView(TemplateView):
    template_name = 'home.html'


@csrf_exempt
def capture_request_view(request, request_id: str):
    save_request_data(request, request_id)
    return render(request, template_name='request_captured.html', context={'url': request_id})


def display_request_data(request, request_id: str):
    context = {'requests': find_requests_by_id(request_id), 'request_id': request_id}
    return render(request, template_name='request_details.html', context=context)
