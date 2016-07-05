"""
Django settings for opsplatform project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import ConfigParser

config = ConfigParser.ConfigParser()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config.read(os.path.join(BASE_DIR, 'opsplatform.conf'))

# ssh config
KEY_DIR = os.path.join(BASE_DIR, 'keys')

# db config
DB_HOST = config.get('db', 'host')
DB_PORT = config.getint('db', 'port')
DB_USER = config.get('db', 'user')
DB_PASSWORD = config.get('db', 'password')
DB_DATABASE = config.get('db', 'database')

GRAPH_DB_HOST = config.get('graph_db', 'host')
GRAPH_DB_PORT = config.get('graph_db', 'port')
GRAPH_DB_USER = config.get('graph_db', 'user')
GRAPH_DB_PASSWORD = config.get('graph_db', 'password')
GRAPH_DB_DATABASE = config.get('graph_db', 'database')


AUTH_USER_MODEL = 'account.User'


# mail config
MAIL_ENABLE = config.get('mail', 'mail_enable')
EMAIL_HOST = config.get('mail', 'email_host')
EMAIL_PORT = config.get('mail', 'email_port')
EMAIL_HOST_USER = config.get('mail', 'email_host_user')
EMAIL_HOST_PASSWORD = config.get('mail', 'email_host_password')
EMAIL_USE_TLS = config.getboolean('mail', 'email_use_tls')
try:
    EMAIL_USE_SSL = config.getboolean('mail', 'email_use_ssl')
except ConfigParser.NoOptionError:
    EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend' if EMAIL_USE_SSL else 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_TIMEOUT = 5


# log config
LOG_DIR = os.path.join(BASE_DIR, 'logs')
SSH_KEY_DIR = os.path.join(BASE_DIR, 'keys/role_keys')
KEY = config.get('base', 'key')
URL = config.get('base', 'url')
LOG_LEVEL = config.get('base', 'log')
IP = config.get('base', 'ip')
PORT = config.get('base', 'port')

# Connect config
try:
    NAV_SORT_BY = config.get('connect', 'nav_sort_by')
except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
    NAV_SORT_BY = 'ip'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yx_32us_6vou8gq9b7y8i1=v!o^8oc5nwba-jn2hb5ho5l*l@0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0/8']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'django_crontab',
    'bootstrapform',

    'opsplatform',
    'account',
    'asset',
    'perm',
    'jlog',
    'monitor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'opsplatform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'opsplatform.context_processors.name_proc',
            ],
        },
    },
]

WSGI_APPLICATION = 'opsplatform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

BOOTSTRAP_COLUMN_COUNT = 10

CRONJOBS = [
    ('0 1 * * *', 'asset.asset_api.asset_ansible_update_all'),
    ('*/10 * * * *', 'jlog.log_api.kill_invalid_connection'),
]

# portal_url URL
PORTAL_URL = 'http://172.16.60.23:5000'

# alarm url
ALARM_URL = 'http://172.16.60.23:9912'


QUERY_ADDR = 'http://172.16.60.23:9966'
