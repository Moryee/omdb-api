from .settings import *

SECRET_KEY = 'test_key'

SIMPLE_JWT = {
    'SIGNING_KEY': SECRET_KEY
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
