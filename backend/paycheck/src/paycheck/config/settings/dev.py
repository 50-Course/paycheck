from .base import *


DEBUG = True

INSTALLED_APPS += []

DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"
DATABASES["default"]["NAME"] = BASE_DIR / "db.sqlite3"

INSTALLED_APPS += ["django-silk"]
