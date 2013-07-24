from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='contact.home'),
<<<<<<< HEAD
	url(r'^submit/$', submit, name='contact.submit'),

=======
	url(r'^submit/$', SubmitView.as_view(), name='contact.submit'),
>>>>>>> fab31bd873737bad9e866b61f581e1716e59b6c3
)
