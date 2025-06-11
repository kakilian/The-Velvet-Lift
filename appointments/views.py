from django.shortcuts import render
from .models import Appointment


def appointment_list(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(user=request.user).order_by('appointment_date')
    else:
        appointments = []

    return render(request, "appointment_list.html", {
        "appointments": appointments
    })
