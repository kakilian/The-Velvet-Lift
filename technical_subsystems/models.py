from django.contrib.auth.models import User
from django.db import models
from base.models import BaseModel

# Create your models here.
# Here to handle User Profiles using model.
class UserProfile(BaseModel):
    """User profile model."""
    user = models.OneToOneField(User, on _delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True)

    def __str__(self):
        return self.user.username
        