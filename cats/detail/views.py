import os
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from cats.detail.models import get_item


class DetailView(TemplateView):
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        instagram_id = self.kwargs['instagram_id']
        item = get_item(instagram_id)

        host = request.environ['HTTP_HOST']
        path_info = request.environ['PATH_INFO']

        context = {
            'item': item,
            'host': host,
            'path_info': path_info,
        }
        return self.render_to_response(context)