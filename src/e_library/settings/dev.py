import os
from .base import *

print("*"*20, "DEVELOPMENT", "*"*20)
ALLOWED_HOSTS = ["*"]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True
# LANGUAGE_CODE = 'en'
# LANGUAGES = [
#     ('en', 'English'),
#     ('hi', 'Hindi'),
# ]

# LANGUAGE_COOKIE_NAME = 'library_lang'
# LOCALE_PATH = (
#     os.path.join(BASE_DIR, 'locale'),
# )

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# STATICFILES_FINDERS = [
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )
# # Custome User Model
# AUTH_USER_MODEL = 'account.User'

# LOGIN_URL = 'account:signin'
# LOGIN_REDIRECT_URL = 'system:home'
# LOGOUT_REDIRECT_URL = 'account:signin'

# # crispy-form
# CRISPY_TEMPLATE_PACK = 'bootstrap4'

# # password Email send
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
# PASSWORD_RESET_TIMEOUT_DAYS = 1

# OTP_TWILIO_ACCOUNT = os.getenv('OTP_TWILIO_ACCOUNT')
# OTP_TWILIO_AUTH = os.getenv('OTP_TWILIO_AUTH')
# OTP_TWILIO_CHALLENGE_MESSAGE = 'OTP send to your number...'
# OTP_TWILIO_TOKEN_TEMPLATE = '''
# \nFrom E_library:please don't share your
# otp: {token}
# '''
# OTP_TWILIO_FROM = os.getenv('OTP_TWILIO_FROM')
# OTP_TWILIO_TOKEN_VALIDITY = 360  # otp valid for 5Min
