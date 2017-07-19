"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("hello.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """ Gets users response about playing a game."""

    answer = request.args.get("game")

    if answer == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Shows user their new madlib."""

    noun = request.args.get("noun")
    color = request.args.get("color")
    person = request.args.get("person")
    adjective = request.args.getlist("adjective")
    verb = request.args.get("verb")
    adverb = request.args.get("adverb")

    return render_template("madlib.html",
                           noun=noun,
                           color=color,
                           person=person,
                           adjective=adjective,
                           verb=verb,
                           adverb=adverb)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
