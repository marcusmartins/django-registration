"""Django settings for tests."""
import os

import django


TEST_ROOT = os.path.join(os.path.normcase(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'supersecret'

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'registration',
]

ROOT_URLCONF = 'tests.urls'

SITE_ID = 1

#MEDIA_URL = '/media/'   # Avoids https://code.djangoproject.com/ticket/21451

#STATIC_ROOT = os.path.join(BASE_DIR, 'tests', 'static')

#STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TEMPLATE_DIRS = (
    os.path.join(TEST_ROOT, 'templates'),
)
print(os.path.join(TEST_ROOT, 'templates'))

if django.VERSION[:2] < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
