"""
Django settings for Dash project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY= 'django-insecure-+g0be&)1(w=^3po)gy44%6s&5-aodgkf5ob#wuc3n3+&@dqc82'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGIN_URL = ''
AUTH_USER_MODEL = 'DashApp.OrAdmin'


ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'DashApp',
    'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'django.middleware.csrf.CsrfViewMiddleware',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


ROOT_URLCONF = 'Dash.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Dash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '139', 
        'HOST': 'db',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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




# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DEFAULT_FROM_EMAIL = 'hajer.hajjaju@gmail.com'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRONJOBS = [
     # Exemple pour appeler une URL toutes les heures
    ('5 21 * * * curl http://localhost:8001/lire-fichiertn1/', 'django_crontab.cron', []),
    ('10 4 1 * * curl http://localhost:8001/lire-fichiertn2/', 'django_crontab.cron', []),
    ('20 4 1 * * curl http://localhost:8001/lire-fichierso/', 'django_crontab.cron', []),
    ('30 4 1 * * curl http://localhost:8001/lire-fichierint/', 'django_crontab.cron', []),  
    ('40 4 1 * * curl http://localhost:8001/lire-fichiertn1epg/', 'django_crontab.cron', []),
    ('50 4 1 * * curl http://localhost:8001/lire-fichiertn2epg/', 'django_crontab.cron', []),            
    ('0 5 1 * * curl http://localhost:8001/lire-fichiersoepg/', 'django_crontab.cron', []),   
    ('10 5 1 * * curl http://localhost:8001/lire-fichiertn2vepg/', 'django_crontab.cron', []), 
    ('20 5 1 * * curl http://localhost:8001/lire-fichiertn1apn/', 'django_crontab.cron', []),
    ('30 5 1 * * curl http://localhost:8001/lire-fichiertn2apn/', 'django_crontab.cron', []),            
    ('40 5 1 * * curl http://localhost:8001/lire-fichiersoapn/', 'django_crontab.cron', []),   
    ('50 5 1 * * curl http://localhost:8001/lire-fichiertn2vepgapn/', 'django_crontab.cron', []),       
]