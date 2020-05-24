from .base import * 

env.read_env(str(APPS_DIR / ".env.production"))

SECRET_KEY = env(
    "SECRET_KEY", default="s*ct5wx%$+6ic#hh)g5kfzh48_bgwos2t1#26v6uk=4us5&+95"
)

DEBUG = env(
    "DEBUG", default="False"
)

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'