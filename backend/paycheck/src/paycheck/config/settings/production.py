from .base import *


CACHES = {}
CACHES["default"]["BACKEND"] = "django.core.cache.backends.redis.RedisCache"
CACHES["default"]["OPTIONS"] = None

DATABASES["default"]["NAME"] = "paycheck-core-prod"
DATABASES["default"]["HOST"] = "paycheck-core-prod"
DATABASES["default"]["USER"] = "paycheck-core-prod"
DATABASES["default"]["PORT"] = 5432
DATABASES["default"]["PASSWORD"] = "paycheck-core-prod"
DATABASES["default"]["OPTIONS"] = {}

DEBUG = False

INSTALLED_APPS += []
