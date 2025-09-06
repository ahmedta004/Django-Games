from django.urls import path
from . import views

app_name = "rps"

urlpatterns = [
    path("", views.play, name="play"),
]
