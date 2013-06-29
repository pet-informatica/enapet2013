from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='information.home'),
	url(r'^events/$', EventView.as_view(), name='information.events'),
	url(r'^city/$', CityView.as_view(), name='information.city'),
	url(r'^infrastructure/$', InfrastructureView.as_view(), name='information.infrastructure'),
	url(r'^meetings/$', MeetingView.as_view(), name='information.meetings'),
)
