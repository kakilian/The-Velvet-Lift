from django.urls import path
from .views import Index


urlpatterns = [path("", Index.as_view(), name="main_features/index.html")]