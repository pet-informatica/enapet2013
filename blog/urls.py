from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='blog.home'),
	url(r'^page/(?P<page>\d+)/$', HomeView.as_view(), name='blog.page'),
    url(r'^(?P<article_id>\d+)/$', ArticleView.as_view(), name='blog_article_id'),
    url(r'^(?P<article_slug>[-\w]+)/$', ArticleView.as_view(), name='blog_article_slug'),
)
