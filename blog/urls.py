from django.conf.urls import url
from .views import IndexView, DetailView


urlpatterns = [
    url(r'^blog/$', IndexView.as_view(), name='index'),
    url(r'^blog/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
]
