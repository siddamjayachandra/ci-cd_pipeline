from flask import Flask, render_template
import random

app = Flask(__name__)

# List of random colors
COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta"]

@app.route("/")
def color_game():
    random_color = random.choice(COLORS)
    return f"""
    <html>
        <head>
            <title>Color Game</title>
        </head>
        <body style="background-color: {random_color}; text-align: center; padding: 50px;">
            <h1 style="color: white;">Guess the Color!</h1>
            <h2 style="color: white;">The background is {random_color}</h2>
            <button onclick="window.location.reload()">Refresh</button>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


