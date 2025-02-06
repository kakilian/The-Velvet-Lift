from django.shortcuts import render


def view_name(request):
    # Your view logic here
    return render(request, "template_profile.html")
