from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from atas.views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='/atas'),
)