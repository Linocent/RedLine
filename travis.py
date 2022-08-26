import os
from concession.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redline',
        'USER': 'concessionaire',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}