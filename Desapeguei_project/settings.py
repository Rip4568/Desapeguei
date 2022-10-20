"""
Django settings for Desapeguei_project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.getenv('DEBUG',default="False")) == 'True'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #configuraões adicionais internos do django
    'django.contrib.humanize',
    #apps instalado pelo django-app
    'Perfil_app',
    'Home_app',
    'Produtos_app',
    'Historico_app',
    'Comentarios_app',
    #dependencias
    'django_extensions',
    'crispy_forms',
    'django_unicorn',
    'star_ratings',
    #allauth configurations
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
"""     'allauth.socialaccount',
    'allauth.socialaccount.providers.google', """

#instalar o whitenoise para a compreensão dos dados
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

ROOT_URLCONF = 'Desapeguei_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Desapeguei_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default":dj_database_url.config(default='postgresql://postgres:admin@localhost:5432/desapeguei_project_db',conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]
""" {
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
    }, """


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles/'

MEDIA_ROOT = '/media/'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REGISTER_REDIRECT_URL = '/'#ao se registrar sera redirecionado para a seguinte url
LOGIN_REDIRECT_URL = '/'#ao fazer login sera redirecionado para a seginte url
SIGNUP_REDIRECT_URL = '/'#ao fazer o registro sera redirecionado para a seguinte url
LOGOUT_REDIRECT_URL = '/'#ao deslogar do site sera redirecionado para a seguinte url

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#Configurações do django-stars
STAR_RATINGS_RERATE = False
STAR_RATINGS_STAR_HEIGHT = 15
STAR_RATINGS_STAR_WIDTH = 15
STAR_RATINGS_ANONYMOUS = False

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"