from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1, story2, story3

app = Flask(__name__)
app.config['SECRET_KEY'] = "ml_sec"

debug = DebugToolbarExtension(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/choice")
def choice():
    """Offer user 3 stories to pick from."""
    return render_template("choice.html")

@app.route("/tall")
def tall():
    """Generate and show form to ask words."""

    blanks = story1.prompts
    return render_template("q01.html", blanks=blanks)

@app.route("/grande")
def grande():
    """Generate and show form to ask words."""

    blanks = story2.prompts
    return render_template("q02.html", blanks=blanks)

@app.route("/venti")
def venti():
    """Generate and show form to ask words."""

    blanks = story3.prompts
    return render_template("q03.html", blanks=blanks)


@app.route("/tale1")
def tall_lib():
    """Show story result."""

    text = story1.generate(request.args)
    return render_template("story1.html", text=text)
 
@app.route("/tale2")
def grande_lib():
    """Show story result."""

    text = story2.generate(request.args)
    return render_template("story2.html", text=text)
 
@app.route("/tale3")
def venti_lib():
    """Show story result."""

    text = story3.generate(request.args)
    return render_template("story3.html", text=text)
 