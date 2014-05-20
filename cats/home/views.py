from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import loader
from django.views.generic import TemplateView
from cats.home.models import get_list

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        item_list = get_list()
        context = {
            'item_list': item_list
        }
        return self.render_to_response(context)