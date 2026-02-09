from flask import Flask, render_template, request
from db import get_db, init_db

app = Flask(__name__)

FLAG_PATH = "/flag.txt"

def load_flag():
    try:
        with open(FLAG_PATH, "r") as f:
            return f.read().strip()
    except Exception:
        return "FLAG_NOT_FOUND"

# Flask 3 compatible init
init_db(load_flag())

@app.route("/", methods=["GET", "POST"])
def search():
    results = []
    error = None
    query_used = ""

    if request.method == "POST":
        term = request.form.get("term", "")

        # 🚨 INTENTIONALLY VULNERABLE 🚨
        query_used = f"SELECT username FROM users WHERE username LIKE '%{term}%'"

        conn = get_db()
        cur = conn.cursor()

        try:
            rows = cur.execute(query_used).fetchall()
            results = [r[0] for r in rows]

            if len(results) == 0:
                error = "User does not exist"

        except Exception as e:
            error = "User does not exist"

    return render_template(
        "search.html",
        results=results,
        error=error,
        query=query_used
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
