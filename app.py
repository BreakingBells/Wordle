from flask import Flask, render_template, request, session, redirect
from wordle_logic import WordleGame
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_game():
    """Load game from session or create a new one."""
    if "game" not in session:
        game = WordleGame()
        session["game"] = game.__dict__
        return game

    game = WordleGame()
    game.__dict__ = session["game"]
    return game

def save_game(game):
    session["game"] = game.__dict__

@app.route("/", methods=["GET", "POST"])
def index():
    game = get_game()
    message = ""

    if request.method == "POST":
        guess = request.form["guess"].strip().lower()

        if len(guess) != 5 or not guess.isalpha():
            message = "Enter a valid 5-letter word."
        else:
            game.check_guess(guess)
            save_game(game)

    return render_template(
        "index.html",
        attempts=game.attempts,
        won=game.is_won(),
        lost=game.is_lost(),
        answer=game.answer.upper(),
        message=message
    )

@app.route("/reset")
def reset():
    session.pop("game", None)
    return redirect("/")
