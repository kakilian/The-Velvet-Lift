from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_name, name="user_profiles"),
]
