from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



MEDIA_URL = 'https://www.bizchool.com/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')

STATIC_URL = "https://www.bizchool.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'mysite', 'staticfiles')
STATICFILES_DIRS = [
 os.path.join(BASE_DIR,  'mysite','static'),
]
