from django.shortcuts import render


# Create your views here.
def user_profiles_view(request):
    return render(request, "profile.html")
