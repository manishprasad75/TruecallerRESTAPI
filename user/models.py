from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    is_spam = models.BooleanField(default=False)
