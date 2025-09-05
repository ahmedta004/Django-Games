from django.urls import path
from . import views

# rps/urls.py
app_name = "rps"

urlpatterns = [
    path("", views.play, name="play"),   # changed from 'rps_game' to 'play'
]
