from django.conf.urls import url
from .views import IndexView, DetailView

urlpatterns = [
    url(r'^star/', IndexView.as_view(), name='index'),
    url(r'^star/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
]