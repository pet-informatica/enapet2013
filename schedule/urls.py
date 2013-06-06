from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='schedule.home'),
    url(r'^(?P<event_id>\d+)/$', EventView.as_view(), name='schedule.event.id'),
    url(r'^(?P<event_slug>[-\w]+)/$', EventView.as_view(), name='schedule.event.slug'),
)
