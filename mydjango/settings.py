"""
Django settings for mydjango project (Clever Cloud ready).
"""

from pathlib import Path
import os

# ------------------------------
# Build paths inside the project
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# Security & Debug
# ------------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-replace-me")
DEBUG = True  # Always False in production

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'app-add66c9a-2357-42d0-be55-7f4ea91e0d65.cleverapps.io',
    'app.nivetha.my-style.in',
    'nivetha.do-style.com',
    'nivetha.fin-tech.com',
]

SECURE_SSL_REDIRECT = True            # Redirect all HTTP to HTTPS
SESSION_COOKIE_SECURE = True          # Only send session cookies over HTTPS
CSRF_COOKIE_SECURE = True 
# ------------------------------
# Installed apps
# ------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
'shop',
    # Your apps
   # Replace 'myapp' with your actual app names

    # Third-party apps
    'django_extensions',
]

# ------------------------------
# Middleware
# ------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mydjango.urls'

# ------------------------------
# Templates
# ------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.cart_item_count',  # custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'mydjango.wsgi.application'

# ------------------------------
# Session settings
# ------------------------------
SESSION_SAVE_EVERY_REQUEST = True

# ------------------------------
# Database (Clever Cloud MySQL)
# ------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'b47cpqpohkil9g059img',
        'USER': 'ubignv77xw0a0qxq',
        'PASSWORD': 'azgIYEbtHT74tYeqvrUp',
        'HOST': 'b47cpqpohkil9g059img-mysql.services.clever-cloud.com',  # e.g., mysql-clevercloud-host.clever-cloud.com
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# ------------------------------
# Password validation
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ------------------------------
# Internationalization
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# Static & Media files
# ------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'shop' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # collectstatic output
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # for production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------
# Login redirects
# ------------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ------------------------------
# Default primary key field type
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'