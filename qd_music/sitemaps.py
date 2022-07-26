from django.contrib.sitemaps import Sitemap
from qd_music.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['homepage', 'booknow']
    def location(self, item):
        return reverse(item)