from pathlib import Path
import os
import environ
import secrets

env = environ.Env()

environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(nbytes=64),
)

DEBUG = True

ALLOWED_HOSTS = []
    
INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app.apps.AppConfig',


    "crispy_forms",
    "crispy_bootstrap5",
    'bootstrap5',
    'fontawesomefree',
    "whitenoise.runserver_nostatic",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'), 
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-  CUSTOM SETTINGS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Used for Custom User Model:
#AUTH_USER_MODEL = 'account.Account'

# limits file size for uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

DATE_INPUT_FORMATS = ['%d-%m-%Y']  # --------------------------- Date format

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = 'dashboard'

LOGOUT_REDIRECT_URL = 'dashboard'

LOGIN_URL = 'login'

JAZZMIN_SETTINGS = {
    'site_title': "App",
    'site_header': "images/logo1.png",
    'site_brand': 'App',
    'site_logo': "images/logo.png",
    'login_logo': "images/logo.png",
    'site_icon': "images/logo.png",
    'login_logo_dark': "images/logo.png",
    "copyright": "12bytes",
    "user_avatar": "images/logo.png",

    "topmenu_links": [
        {"name": "Admin Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "auth.user"},
        {"name": "Site Home", "url": "/admin/logout", "redirect": "/home/"}
    ]
}

# Select your Jazzmin theme here:  https://django-jazzmin.readthedocs.io/ui_customisation/
JAZZMIN_UI_TWEAKS = {
    "theme": "lux",
    "dark_mode_theme": "darkly",
}

#=-=-=-=-=-=-=-=-=-=-=-=-=->  PRODUCTION SETTINGS:  Remove all # below

# WHITENOISE_USE_FINDERS = True

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#CSRF_COOKIE_SECURE = True

#SESSION_COOKIE_SECURE = True


# Remove the '#' to require SSL connections Leave it in for localhost
#SECURE_SSL_REDIRECT = True