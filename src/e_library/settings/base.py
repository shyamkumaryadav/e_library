import os


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'hldcqlh=m&4qiweblwoaap&-z_-+av@37sp2by-1fizn=6*!(u'

DEBUG = True

ALLOWED_HOSTS = ['*']

# AUTHENTICATION_BACKENDS = [

#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',

# ]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Django allauth
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',

    # Django Extensions
    'django_extensions',
    'import_export',
    'django_cleanup',

    # Django-Rest
    'rest_framework',

    # Crispy Form is Best
    'crispy_forms',

    # otp django
    'django_otp',
    'otp_twilio',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_hotp',

    # myApps
    'account',
    'system',
]

# SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',  # Django-otp
]

ROOT_URLCONF = 'e_library.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'e_library.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
]

LANGUAGE_COOKIE_NAME = 'library_language'

LOCALE_PATH = (
    os.path.join(BASE_DIR, 'locale'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Custome User Model
AUTH_USER_MODEL = 'account.User'

LOGIN_URL = 'account:signin'
LOGIN_REDIRECT_URL = 'system:home'
LOGOUT_REDIRECT_URL = 'account:signin'

# crispy-form
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# password Email send


# OPT TWILIO
OTP_TWILIO_ACCOUNT = os.getenv('OTP_TWILIO_ACCOUNT')
OTP_TWILIO_AUTH = os.getenv('OTP_TWILIO_AUTH')
OTP_TWILIO_CHALLENGE_MESSAGE = 'OTP send to your number...'
OTP_TWILIO_TOKEN_TEMPLATE = '''
\nFrom E_library:please don't share your
otp: {token}
'''
OTP_TWILIO_FROM = os.getenv('OTP_TWILIO_FROM')
OTP_TWILIO_TOKEN_VALIDITY = 300  # otp valid for 5Min (5*60)
