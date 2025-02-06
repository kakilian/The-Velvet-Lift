from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Here is where the appointments will be managed.


class Appointment(models.Model):
    """Model for user appointments."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        "user_profiles.Doctor", on_delete=models.SET_NULL, null=True
    )
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
        """Doctor must here identify themselves by logging in"""
        if self.doctor:
            return f"Appointment with {self.doctor.user.username} on {self.appointment_date}"
        return f"Appointment on {self.appointment_date}"


class Payment(models.Model):
    """Model for tracking payments for appointments."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.OneToOneField(
        Appointment, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("completed", "Completed")],
        default="pending",
    )

    def __str__(self):
        return f"Payment {self.id} - {self.status}"
