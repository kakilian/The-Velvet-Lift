from django.db import models
from django.contrib.auth.models import User
from technical_subsystems.models import UserProfile
from main_features.models import BaseModel

# Create your models here.
# Here is where the appointments will be managed.


class Appointment(BaseModel):
    """Model for user appointments."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("completed", "Completed"),
        ],
        default="pending",
    )

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.appointment_date}"
