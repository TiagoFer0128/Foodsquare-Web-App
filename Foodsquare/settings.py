"""
Django settings for FoodSquare project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=%m4l_6pi$++(nf7th-z(dz)f(!uwhv&dm1w*5t*l37m+09wlx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '192.168.137.1', 'localhost', 'www.localhost', 'manager.localhost', 'api.localhost', 'admin.localhost',
                 'foodsquare.com', 'www.foodsquare.com', 'manager.foodsquare.com', 'api.foodsquare.com',
                 'foodsquare.net', 'www.foodsquare.net', 'manager.foodsquare.net', 'api.foodsquare.net',
                 'admin.foodsquare.com']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',

	'browse',
	'accounts',
	'manager',
	'webAdmin',
	'rest_framework',
	'customer',
	'debug_toolbar',
	'django_extensions',

	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.facebook',
	'allauth.socialaccount.providers.google',
	'sslserver',

	'location_field.apps.DefaultConfig',
	'phonenumber_field',
	'django_hosts',
]

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

MIDDLEWARE = [
	'django_hosts.middleware.HostsRequestMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'Foodsquare.urls'
ROOT_HOSTCONF = 'Foodsquare.hosts'

DEFAULT_HOST = 'www'
# PREPEND_WWW = True

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
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

WSGI_APPLICATION = 'Foodsquare.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AUTHENTICATION_BACKENDS = (
	"django.contrib.auth.backends.ModelBackend",
	"allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = \
	{'facebook':
		 {'METHOD': 'oauth2',
		  'SCOPE': ['email', 'public_profile', 'user_friends'],
		  'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
		  'FIELDS': [
			  'id',
			  'email',
			  'name',
			  'first_name',
			  'last_name',
			  'verified',
			  'locale',
			  'timezone',
			  'link',
			  'gender',
			  'updated_time'],
		  'EXCHANGE_TOKEN': True,
		  'LOCALE_FUNC': lambda request: 'kr_KR',
		  'VERIFIED_EMAIL': False,
		  'VERSION': 'v2.4'}}


AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = '/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SITE_ID = 1
