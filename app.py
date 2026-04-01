from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Временное хранилище сообщений
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "username" not in session:
        session["username"] = request.form["username"]
        return redirect("/")
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    if "username" in session:
        text = request.form["text"]
        messages.append({
            "username": session["username"],
            "text": text
        })
    return redirect("/")

@app.route("/messages")
def get_messages():
    return render_template("messages.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)