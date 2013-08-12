from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import index, status, profile, my_profile

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^status$', status),
    url(r'^(favicon\.ico)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^zen/$', 'zen.views.index', name='zen'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', my_profile, name="me"),
    url(r'^users/.*$', profile, name='profile'),

)
