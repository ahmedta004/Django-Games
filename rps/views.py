from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import random

def play(request):
    choices = ["rock", "paper", "scissors"]
    user_choice = request.GET.get("choice")
    computer_choice = random.choice(choices)
    result = None

    if user_choice:
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
        else:
            result = "Computer wins!"

    return render(request, "rps/game.html", {
        "user_choice": user_choice,
        "computer_choice": computer_choice if user_choice else None,
        "result": result,
    })
