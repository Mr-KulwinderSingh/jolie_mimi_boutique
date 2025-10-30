from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    default_acl = 'public-read'
    file_overwrite = True  # Optional — static files can safely overwrite


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    default_acl = 'public-read'  # ensure uploaded files are readable
    file_overwrite = False       # prevents overwriting user uploads
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN  # ensures correct URLs
