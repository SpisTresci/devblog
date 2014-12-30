from __future__ import unicode_literals

SECRET_KEY = "b86ac743-6564-446b-9e69-b6bc84886f72e341d28e-54be-44df-b467-73985e0d6c1c391a5209-4e67-466e-a5de-5368c9dcef92"
NEVERCACHE_KEY = "fd3dd1c2-0ad9-40e0-b384-8a952f2d309a62e310c9-010c-4cd6-be18-7c4ea1dfe7cacb70a3a8-cefe-4c86-92af-83b990fa6017"
ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "mysecretpassword",
        "HOST": "db",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "mezzanine-project"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
