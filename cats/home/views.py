from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
from cats.home.models import get_list, get_json


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        item_list, next = get_list()

        request.session['next'] = next

        host = request.environ['HTTP_HOST']
        path_info = request.environ['PATH_INFO']

        context = {
            'item_list': item_list,
            'host': host,
            'path_info': path_info,
            }
        return self.render_to_response(context)


class DoesNotExist(object):
    pass


def home_json(request):

    try:
        json, next = get_json(request.session['next'])
    except Exception as e:
        print str(e)
        return HttpResponseNotFound(content_type='application/json')

    request.session['next'] = next
    return HttpResponse(json, content_type='application/json')