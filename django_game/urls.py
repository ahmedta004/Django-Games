from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # homepage
    path("tictactoe/", include("tictactoe.urls")),  # tic tac toe
    path("rps/", include("rps.urls")),              # rock paper scissors
    path("guess/", include("guess.urls")),          # number guessing game
]

# Ensure this HTML code is moved to the appropriate template file (e.g., home.html).
