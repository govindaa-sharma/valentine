from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move_no")
def move_no():
    """Generates a random position for the No button."""
    new_x = random.randint(50, 300)
    new_y = random.randint(50, 250)
    return {"x": new_x, "y": new_y}

if __name__ == "__main__":
    app.run(debug=True)
