INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'chats',  # your app
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
