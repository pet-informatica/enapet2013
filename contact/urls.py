from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='contact.home'),

	url(r'^submit/$', SubmitView.as_view(), name='contact.submit'),
)
