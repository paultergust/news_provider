from news_provider.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_api_dev',
        'USER': 'news_api_dev',
        'PASSWORD': 'news_api_dev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
