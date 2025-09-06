from django.urls import path
from . import views
app_name = "guess"
urlpatterns = [
    path("new/", views.start_game, name="start"),
    path("", views.play, name="play"),
]
