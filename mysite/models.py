from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UsersContact(models.Model):
    synced_from_uid = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)


class UserSpam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    class Meta:
        unique_together = ("user", "phone")
