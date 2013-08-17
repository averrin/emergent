from django.conf import settings
from django.conf.urls import patterns, include, url
from views import IndexView, StatusView, ProfileView, MyProfileView

from django.contrib.auth import views as auth_views

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
    url(r'^rpg/', include('rpg.urls'), name='rpg'),
    url(r'^users/(?P<username>.*)/$', ProfileView.as_view(), name='profile'),
    url(r'^account/', include('social_auth.urls')),
    url(r'^account/logout/$', auth_views.logout, {'next_page': '/'}, name='auth_logout'),
    url(r'^account/profile/$', MyProfileView.as_view(), name='me'),

)
