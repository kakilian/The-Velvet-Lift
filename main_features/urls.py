from django.urls import path
from .views import Index


urlpatterns = [path("", Index, name="main_features")]
