from .base import *  

env.read_env(str(APPS_DIR / ".env.local"))
SECRET_KEY = env(
    "SECRET_KEY", default="s*ct5wx%$+6ic#hh)g5kfzh48_bgwos2t1#26v6uk=4us5&+95"
)
import mimetypes
mimetypes.init()
mimetypes.types_map['.css'] = 'text/css'

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/db.sqlite3'),
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs
# .djangoproject.com/en/3.0/howto/static-files/
print(BASE_DIR)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")