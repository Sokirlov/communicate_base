import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(__file__)
SECRET_KEY = 'django-insecure-ja4f&pac_+&-*09m1*--%g7vm7!%0s%1-+_4a6()yic8zk=u)#'

DEBUG = True

ALLOWED_HOSTS = ['192.168.37.71', '127.0.0.1', '192.168.37.125']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dgf',
            'USER' : 'root',
            'PASSWORD' : '',
            'default-character-set' : 'utf8',
            'HOST' : 'localhost',
            # 'PORT' : '5432',
        }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')