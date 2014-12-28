
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "b86ac743-6564-446b-9e69-b6bc84886f72e341d28e-54be-44df-b467-73985e0d6c1c391a5209-4e67-466e-a5de-5368c9dcef92"
NEVERCACHE_KEY = "fd3dd1c2-0ad9-40e0-b384-8a952f2d309a62e310c9-010c-4cd6-be18-7c4ea1dfe7cacb70a3a8-cefe-4c86-92af-83b990fa6017"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
