from django.shortcuts import render, redirect
import random
from core.models import GuessGame

def start_game(request):
    request.session["number"] = random.randint(1, 100)
    request.session["attempts"] = 0
    return redirect("guess:play")

def play(request):
    number = request.session.get("number")
    attempts = request.session.get("attempts", 0)
    feedback = None
    guess = None

    if request.method == "POST":
        try:
            guess = int(request.POST.get("guess"))
        except (TypeError, ValueError):
            guess = None

        attempts += 1
        request.session["attempts"] = attempts

        if guess is None:
            feedback = "Enter a valid number."
        elif guess < number:
            feedback = "Too low!"
        elif guess > number:
            feedback = "Too high!"
        else:
            feedback = f"🎉 Correct! You guessed it in {attempts} tries."
            # Save game
            GuessGame.objects.create(secret_number=number, attempts=attempts, success=True, player=None)
            # Optionally clear session or keep it
            # del request.session['number']
            # del request.session['attempts']

    return render(request, "guess/game.html", {
        "feedback": feedback,
        "guess": guess,
        "attempts": attempts,
    })
