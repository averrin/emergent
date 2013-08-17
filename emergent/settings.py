# Django settings for emergent_dev project.
import os
try:
    from my_settings import PROJECT_PATH
except ImportError:
    import os.path as _p
    PROJECT_PATH = _p.dirname(_p.dirname(_p.abspath(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'emergent.sqlite3'),
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Omsk'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = USE_L10N = USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static_dev'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'icytr!zq2c*kghq@60y+lvc2e+8@_emvp=r9n$@ziga64whqpj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'emergent.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'emergent.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'social_auth',
    'django_extensions',
    'djangobower',
    'django_extensions',
    'emergent',
    'zen',
    'rpg',

)

ACCOUNT_ACTIVATION_DAYS = 7
BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_PATH, 'components/')

BOWER_INSTALLED_APPS = (
    'bootstrap',
)

AUTH_USER_MODEL = 'rpg.Hero'
LOGIN_URL = 'login'

# Social Auth settings {{{

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
SOCIAL_AUTH_ERROR_KEY             = 'socialauth_error'
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

GITHUB_APP_ID                     = ''
GITHUB_API_SECRET                 = ''

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',

    'social_auth.backends.pipeline.user.update_user_details',
)

# Social Auth settings {{{
