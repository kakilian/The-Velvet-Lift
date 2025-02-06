from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""Model to record any transformation images for Cosmetic procedures."""


class Transformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    before_image = models.ImageField(upload_to="transformations/")
    after_image = models.ImageField(upload_to="transformations/")
    procedure = models.CharField(max_length=100)

    def __str__(self):
        return f"Transformation for {self.user.username}"
