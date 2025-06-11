from django.shortcuts import render

def book_appointment(request):
    """
    View to handle booking an appointment.
    """
    if request.method == "POST":
        # Handle form submission logic here
        pass
    return render(request, "appointments/book_appointment.html")