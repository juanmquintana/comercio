from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ipap',
        'USER': 'postgres',
        'PASSWORD': 'linka21',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}