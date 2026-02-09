from flask import Flask, render_template, request, redirect, session
from db import init_db, get_db

app = Flask(__name__)
app.secret_key = "dev-secret-key"

FLAG_PATH = "/flag.txt"

def load_flag():
    try:
        with open(FLAG_PATH, "r") as f:
            return f.read().strip()
    except Exception:
        return "FLAG_NOT_FOUND"

FLAG = load_flag()

# ✅ Flask 3 compatible
init_db()

@app.route("/")
def index():
    if session.get("user"):
        return redirect("/dashboard")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # 🚨 INTENTIONALLY VULNERABLE SQL 🚨
    query = f"SELECT username FROM users WHERE username = '{username}' AND password = '{password}'"

    conn = get_db()
    cur = conn.cursor()

    try:
        user = cur.execute(query).fetchone()
    except Exception as e:
        return render_template("login.html", error=f"SQL error: {e}")

    if user:
        session["user"] = user[0]
        return redirect("/dashboard")

    return render_template("login.html", error="Invalid credentials")

@app.route("/dashboard")
def dashboard():
    user = session.get("user")
    if not user:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        user=user,
        is_admin=(user == "admin"),
        flag=FLAG
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
