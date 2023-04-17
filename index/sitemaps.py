from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    
    def items(self):
        return ['index', 'estimate','privacy','tos','register']

    def location(self, item):
        return reverse(item)