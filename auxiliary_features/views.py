from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def appointment_list(request):
    return HttpResponse("This is the appointment list page")
