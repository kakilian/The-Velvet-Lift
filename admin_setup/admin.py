from django.contrib import admin
from user_profiles.models import UserProfile, Doctor
from appointments.models import Appointment, Payment
from transformations.models import Transformation

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Transformation)
