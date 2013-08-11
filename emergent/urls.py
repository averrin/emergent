from django.conf import settings
from django.conf.urls import patterns, include, url
from emergent.views import index, status

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^status$', status),
    url(r'^(favicon\.ico)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^zen/$', 'zen.views.index', name='zen'),
)
