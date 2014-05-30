from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView
from cats.home.models import get_list

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        item_list = get_list()

        host = request.environ['HTTP_HOST']
        path_info = request.environ['PATH_INFO']

        context = {
            'item_list': item_list,
            'host': host,
            'path_info': path_info,
        }
        return self.render_to_response(context)