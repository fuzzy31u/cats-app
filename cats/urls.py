from django.conf.urls import patterns, include, url

from django.contrib import admin
from cats.detail.views import DetailView
from cats.home.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<instagram_id>(\d|_)+)$', DetailView.as_view(), name='detail'),
)
