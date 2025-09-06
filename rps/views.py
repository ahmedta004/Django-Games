from django.shortcuts import render
import random
from core.models import RpsGame, Player  # import models

def play(request):
    choices = ["rock", "paper", "scissors"]
    user_choice = request.GET.get("choice")
    computer_choice = None
    result = None

    if user_choice:
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            result = "Draw"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "Win"
        else:
            result = "Lose"

        # Save to DB (player is optional; left null for now)
        RpsGame.objects.create(
            player=None,
            player_choice=user_choice,
            computer_choice=computer_choice,
            result=result
        )

    return render(request, "rps/game.html", {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
    })
