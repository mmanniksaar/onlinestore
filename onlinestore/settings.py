import os
from pathlib import Path
#from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = '505ktt=5@g=h$rpd9%^i@wis-2xg7k8mclqj9o@nzupy@oadq)'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG', cast=bool)
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.onlinestore-700.herokuapp.com', 'onlinestore-700.com', 'www.onlinestore-700.com']

# Application definition
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'cloudinary',
    'location_field.apps.DefaultConfig',
]


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'do303mku5',
    'API_KEY': '359622687652815',
    'API_SECRET': '7wXzvmvueHOxgXLwSvdPhA2gYtQ',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlinestore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links', #now context_processors is available in all templates
                'carts.context_processors.counter', #now context_processors is available in all templates
            ],
        },
    },
]


# only if django version >= 3.0
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

WSGI_APPLICATION = 'onlinestore.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(BASE_DIR / 'db.sqlite3'),
#     }
# }

# Password validation
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

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATICFILES_DIRS = [
    'onlinestore/static',
]
#media files conf
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media/'

#SMTP config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'onlinestorez700@gmail.com'
EMAIL_HOST_PASSWORD = '+mSd5Ti--dQvWaRr'
EMAIL_USE_TLS = True

LOCATION_FIELD = {
 #   'provider.google.api': '//maps.google.com/maps/
    #  api/js?sensor=false',
    'map.provider': 'google',
    'map.zoom': 7,
    'search.provider': 'google',
    'search.suffix': '',
    'provider.google.api_key': 'AIzaSyCJjrJOth0XfqOEv6SY8y7uNYdAfkFTwLI',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',
}

if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
