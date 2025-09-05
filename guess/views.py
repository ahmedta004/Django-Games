from django.shortcuts import render, redirect
import random

def start_game(request):
    # Initialize the game
    request.session["number"] = random.randint(1, 100)
    request.session["attempts"] = 0
    return redirect("guess:guess_play")

def play(request):
    number = request.session.get("number")
    attempts = request.session.get("attempts", 0)
    feedback = None
    guess = None

    if request.method == "POST":
        guess = int(request.POST.get("guess"))
        attempts += 1
        request.session["attempts"] = attempts

        if guess < number:
            feedback = "Too low!"
        elif guess > number:
            feedback = "Too high!"
        else:
            feedback = f"🎉 Correct! You guessed it in {attempts} tries."

    return render(request, "guess/game.html", {
        "feedback": feedback,
        "guess": guess,
        "attempts": attempts,
    })
