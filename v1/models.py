# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    ext_id = models.CharField(max_length=255, null=True)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    service_name = models.CharField(max_length=255, null=True)
    stage = models.CharField(max_length=255, null=True)

    external_user_id = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    ip = models.GenericIPAddressField(null=True)
    mac = models.CharField(max_length=255, null=True)
    imei = models.CharField(max_length=255, null=True)
    device_model = models.CharField(max_length=255, null=True)

    date = models.DateTimeField(auto_now_add=True)
