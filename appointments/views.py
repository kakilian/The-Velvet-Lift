from django.shortcuts import render


def appointment_list(request):
    # Fallback hardcoded data for visual output
    appointments = [
        {"appointment_date": "2025-06-15 10:00", "status": "Confirmed"},
        {"appointment_date": "2025-06-18 14:30", "status": "Pending"},
    ]

    return render(request, "appointments/appointment_list.html", {
        "appointments": appointments
    })