from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import datetime, timedelta

from .generators import generate_client_id, generate_client_secret


class Application(models.Model):
    """[Application model which stores the client id and client secret which we provide\
        for an application to consume our Rest API.]

    Arguments:
        models {[model]} -- [Each model is a Python class that subclasses django.db.models.Model.]

    Returns:
        [model] -- [Each attribute of the model represents a database field.]
    """
    client_id = models.CharField(
        max_length=100, unique=True, default=generate_client_id, db_index=True
    )
    client_secret = models.CharField(
        max_length=100, unique=True, default=generate_client_id, db_index=True
    )
    application_name = models.CharField(max_length=255)
    activate = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.application_name


class AuthToken(models.Model):
    """[Model which stored the access token for different application that is added to our DB]

    Arguments:
        models {[model]} -- [Each model is a Python class that subclasses django.db.models.Model.]

    Returns:
        [model] -- [Each attribute of the model represents a database field.]
    """
    access_token = models.CharField(max_length=100, unique=True)
    refresh_token = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateTimeField()
    refresh_token_expiry = models.DateTimeField()
    expired = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    application = models.OneToOneField(
        Application, on_delete=models.CASCADE, related_name="app_name", primary_key=True
    )
    def __str__(self):
        return self.application

