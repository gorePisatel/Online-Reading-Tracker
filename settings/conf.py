from decouple import config


SECRET_KEY = config('PROJECT_SECRET_KEY', default='default-secret-key', cast=str)
ENV_ID = config('PROJECT_ENV_ID', default='dev', cast=str)
ALLOWED_ENV_ID = ('dev', 'prod')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

CORS_ALLOW_ALL_ORIGINS = True
