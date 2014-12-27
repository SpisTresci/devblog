
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "2a239f12-7259-4795-b53a-4e83912b1eac9b5e3479-6486-4287-8728-9145e27f2d518b4c92bc-0473-400d-b2ce-758c5a095450"
NEVERCACHE_KEY = "91cfe117-949b-4913-898b-1944c889a76b6493b354-5a37-4b8a-8f76-4349ae98bf174ed4f307-b23f-4161-975a-96695e1c2088"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'db',
        'PORT': 5432,
    }
}

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "SSH_USER": "root",  # SSH username for host deploying to
#     "HOSTS": 'localhost:20022',  # List of hosts to deploy to (eg, first host)
#     "DOMAINS": ['localhost'],  # Domains for public site
#     "REPO_URL": "https://github.com/SpisTresci/devblog.git",  # Project's repo URL
#     "VIRTUALENV_HOME":  "/env",  # Absolute remote path for virtualenvs
#     "PROJECT_NAME": "mezzanine",  # Unique identifier for project
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "GUNICORN_PORT": 8000,  # Port gunicorn will listen on
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": DATABASES['default']['PASSWORD'],  # Live database password
#     "ADMIN_PASS": "root",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
