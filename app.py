from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

# ⚠️ secret key needed for session
app.secret_key = "secret123"


@app.route("/")
def home():
    # 👉 first time open → game start
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["chances"] = 5

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    user = int(request.form["user_input"])
    
    number = session["number"]
    chances = session["chances"]

    # 👉 decrease chance
    chances -= 1
    session["chances"] = chances

    if user == number:
        result = "🎉 Correct! You won!"
        session.clear()   # reset game

    elif chances == 0:
        result = f"💀 You lost! Number was {number}"
        session.clear()

    elif user > number:
        result = "📈 Too High!"

    else:
        result = "📉 Too Low!"

    return render_template("index.html", result=result, chances=chances)


if __name__ == "__main__":
    app.run(debug=True)