from .base import *


CACHES = {}
CACHES["default"]["BACKEND"] = "django.core.cache.backends.redis.RedisCache"
CACHES["default"]["OPTIONS"] = None
