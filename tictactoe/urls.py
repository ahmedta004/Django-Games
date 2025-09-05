# tictactoe/urls.py
from django.urls import path
from . import views

app_name = 'tictactoe'

urlpatterns = [
    path('', views.index, name='index'),          # home / start page
    path('new/', views.new_game, name='new_game'),# start a new game
    path('game/', views.game, name='game'),      # show board
    path('move/<int:pos>/', views.move, name='move'),  # make move (POST)
    path('reset/', views.reset, name='reset'),   # clear session
]
