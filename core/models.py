from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"Player {self.pk}"

class RpsGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    player_choice = models.CharField(max_length=20)
    computer_choice = models.CharField(max_length=20)
    result = models.CharField(max_length=20)  # "Win", "Lose", "Draw"
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RPS #{self.pk} - {self.result}"

class GuessGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
    success = models.BooleanField(default=False)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Guess #{self.pk} - {'Success' if self.success else 'Failed'}"

class TicTacToeGame(models.Model):
    # Players are optional for local play
    player_x = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True, related_name="tictactoe_x")
    player_o = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True, related_name="tictactoe_o")
    winner = models.CharField(max_length=5, blank=True, null=True)  # 'X', 'O', 'Draw', or ''
    board_state = models.CharField(max_length=9, blank=True, default="")  # store 9-char board like "XOX_O____"
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TicTacToe #{self.pk} - {self.winner or 'ongoing'}"
