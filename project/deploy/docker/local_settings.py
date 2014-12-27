from __future__ import unicode_literals

SECRET_KEY = "2a239f12-7259-4795-b53a-4e83912b1eac9b5e3479-6486-4287-8728-9145e27f2d518b4c92bc-0473-400d-b2ce-758c5a095450"
NEVERCACHE_KEY = "91cfe117-949b-4913-898b-1944c889a76b6493b354-5a37-4b8a-8f76-4349ae98bf174ed4f307-b23f-4161-975a-96695e1c2088"
ALLOWED_HOSTS = ['localhost']

DEBUG = True

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "postgres",
        # Not used with sqlite3.
        "USER": "postgres",
        # Not used with sqlite3.
        "PASSWORD": "mysecretpassword",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "db",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "mezzanine"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"