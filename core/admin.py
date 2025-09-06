from django.contrib import admin
from .models import Player, RpsGame, GuessGame, TicTacToeGame

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')

@admin.register(RpsGame)
class RpsGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'player_choice', 'computer_choice', 'result', 'played_at')
    list_filter = ('result',)

@admin.register(GuessGame)
class GuessGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'secret_number', 'attempts', 'success', 'played_at')
    list_filter = ('success',)

@admin.register(TicTacToeGame)
class TicTacToeAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_x', 'player_o', 'winner', 'played_at')
