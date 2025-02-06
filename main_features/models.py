from django.db import models


# Create your models here.
# Reusable fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        """Using True ensures it wont create its own table"""
