from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Using Profiles on APP Application


class UserProfile(models.Model):
    """For Private User"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    """For Doctor and Cosmetic Staff"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"
