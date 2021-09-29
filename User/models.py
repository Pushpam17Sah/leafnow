from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    doy = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    suggestion = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
