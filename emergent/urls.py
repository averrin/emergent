from django.conf import settings
from django.conf.urls import patterns, include, url
from views import IndexView, StatusView, ProfileView, MyProfileView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^status$', StatusView.as_view(), name='status'),
    url(r'^(favicon\.ico)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^zen/', include('zen.urls'), name='zen'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', MyProfileView.as_view(), name="me"),
    url(r'^users/.*$', ProfileView.as_view(), name='profile'),

)
