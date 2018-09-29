from .settings import *
import dj_database_url

if os.environ.get('debug', False):
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
