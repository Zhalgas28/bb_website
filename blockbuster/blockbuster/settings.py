import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-mo*--75p%8i!$)w1#5!--p)ty_oymamn$szl#o9v*y6u+1udi9'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'social_django',
    'app.apps.AppConfig',
    'contact.apps.ContactConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'blockbuster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'blockbuster.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blockbuster_db',
        'USER': 'zhalgas',
        'PASSWORD': 'zhalgas',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Аутентификация

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',  # бекенд авторизации через ВКонтакте
    'django.contrib.auth.backends.ModelBackend',  # бекенд классической аутентификации
    'social_core.backends.google.GoogleOAuth2',  # бэкенд авторизации через Гугл
    'social_core.backends.facebook.FacebookOAuth2',
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_VK_OAUTH2_KEY = '8124520'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '04RIW4ToA55Wid1mNdWy'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_FACEBOOK_KEY = '388750916403353'
SOCIAL_AUTH_FACEBOOK_SECRET = '55b14ced28b3c6511a95fef738da2e1b'

# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

LOGIN_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app/static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

INTERNAL_IPS = [
    "127.0.0.1",
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
    }
}

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'blackhorse11zhalgas@gmail.com'
EMAIL_HOST_PASSWORD = 'manutd11zhalgas'
EMAIL_PORT = 465
