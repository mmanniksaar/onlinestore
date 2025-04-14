import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import cloudinary
from django.contrib.messages import constants as messages

load_dotenv()


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'cloudinary_storage',
    'cloudinary',
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
    'location_field.apps.DefaultConfig',
]


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
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



X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

WSGI_APPLICATION = 'onlinestore.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'


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

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATICFILES_DIRS = [
    'onlinestore/static',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media/'

EMAIL_HOST = os.environ.get('EMAIL_HOST_NAME')
EMAIL_PORT = os.environ.get('EMAIL_PORT_NUMBER')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PWD')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS_STATE')



LOCATION_FIELD = {
 #   'provider.google.api': '//maps.google.com/maps/
    #  api/js?sensor=false',
    'map.provider': 'google',
    'map.zoom': 7,
    'search.provider': 'google',
    'search.suffix': '',
    'provider.google.api_key': os.getenv('GOOGLE_API_KEY'),
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',
}

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.config()}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

cloudinary.config( 
    cloud_name = os.getenv('CLOUD_NAME'), 
    api_key = os.getenv('API_KEY'), 
    api_secret = os.getenv('API_SECRET') 
)