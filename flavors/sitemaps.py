from django.contrib.sitemaps import Sitemap
from .models import Flavor
from django.core.urlresolvers import reverse
from django.contrib import sitemaps


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main', 'about', 'license']

    def location(self, item):
        return reverse(item)


class FlavorSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Flavor.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
