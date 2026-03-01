import os
from pathlib import Path
import dj_database_url

# Only load .env file in local development (not on Heroku)
if 'DYNO' not in os.environ:  # Heroku automatically sets DYNO
    from dotenv import load_dotenv
    load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '&r-x2$m&wr&av4@wvhxah6(#6ar$nob)c*6f0j!2t!xy7ej2^8')


DEBUG = 'DEVELOPMENT' in os.environ


ALLOWED_HOSTS = [
    '8000-mrkulwinder-joliemimibo-9n7kj185axd.ws-eu121.gitpod.io',
    'jolie-mimi-boutique-ad3e13f83c61.herokuapp.com',
    'localhost',
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'products',
    'cart',
    'checkout',
    'profiles',
    'wishlist',
    'jolie_mimi_boutique',

    # Other
    'crispy_forms',
    'storages',
    'anymail',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jolie_mimi_boutique.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'jolie_mimi_boutique.wsgi.application'

# Database
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

CSRF_TRUSTED_ORIGINS = [
    'https://8000-mrkulwinder-joliemimibo-9n7kj185axd.ws-eu121.gitpod.io',
    'https://jolie-mimi-boutique-ad3e13f83c61.herokuapp.com',
]

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS S3 Configuration
if os.environ.get('USE_AWS') == 'True':
    print("✓ Using AWS S3 storage")  # This will show in logs
    # S3 Configuration
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'jolie-mimi-boutique-bucket'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_SIGNATURE_VERSION = "s3v4"


    # Static and media files
    STATICFILES_STORAGE = 'jolie_mimi_boutique.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'jolie_mimi_boutique.custom_storages.MediaStorage'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'eur'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

# Email settings
if 'DEVELOPMENT' in os.environ:
    # Local development: print emails to console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'joliemimiboutique@gmail.com'
else:
    # Production (Heroku) - SendGrid setup
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = "apikey"
    EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")
    DEFAULT_FROM_EMAIL = "joliemimiboutique@gmail.com"
    SERVER_EMAIL = "joliemimiboutique@gmail.com"

ACCOUNT_ADAPTER = 'jolie_mimi_boutique.adapters.NoPrefixAccountAdapter'


# # Email settings
# if 'DEVELOPMENT' in os.environ:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#     DEFAULT_FROM_EMAIL = 'joliemimiboutique@gmail.com'
# else:
#     # Production (Heroku) - SendGrid via SMTP
#     EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#     EMAIL_HOST = "smtp.sendgrid.net"
#     EMAIL_PORT = 587
#     EMAIL_USE_TLS = True
#     EMAIL_HOST_USER = "apikey"
#     EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")

#     DEFAULT_FROM_EMAIL = "joliemimiboutique@gmail.com"
#     SERVER_EMAIL = "joliemimiboutique@gmail.com"