import os
from .base import *

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static"),
]

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