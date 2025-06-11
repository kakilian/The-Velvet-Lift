from django.contrib import admin
from .models import Appointment

admin.site.unregister(Appointment)  # Unregister first to start fresh


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("user", "doctor", "appointment_date", "status")
    list_filter = ("status", "appointment_date")
    search_fields = ("user__username", "doctor__user__username")