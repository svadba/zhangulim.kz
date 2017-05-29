from django.conf.urls import url
from .views import IndexView, DetailView

urlpatterns = [
    url(r'^album/$', IndexView.as_view(), name='albums'),
    url(r'^album/(?P<album>[-\w]+)/$', DetailView.as_view(), name='detail_album'),
]