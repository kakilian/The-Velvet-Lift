from django.contrib import admin
from .models import Appointment


# Check if it's already registered to avoid the error
if Appointment not in admin.site._registry:
    #@admin.register(Appointment)
    class AppointmentAdmin(admin.ModelAdmin):
        list_display = ("user", "doctor", "appointment_date", "status")
        list_filter = ("status", "appointment_date")
        search_fields = ("user__username", "doctor__user__username")
