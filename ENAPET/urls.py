from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from home.views import IndexView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='home.home'),
	url(r'^news/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('schedule.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^information/', include('information.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^publications/', include('publications.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
)

from django.conf import settings

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
