from django.conf.urls import url
from flavors.views import IndexView, flavor_detail, flavor_detail1, thanks
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .models import Flavor
from .sitemaps import StaticViewSitemap

info_dict = {
    'queryset': Flavor.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^send/$', flavor_detail, name='send_telegram'),
    url(r'^thanks/', thanks, name='thanks'),
    url(r'^flavor/(?P<flavor_id>[0-9]+)/$', flavor_detail1, name='flor'),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'flavor': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
