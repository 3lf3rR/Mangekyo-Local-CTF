from flask import Flask, request, make_response, render_template
import base64
import json

app = Flask(__name__)

# XOR key (server-side secret)
XOR_KEY = b"simplekey"

def xor_data(data: bytes, key: bytes) -> bytes:
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])


@app.route("/")
def index():

    user = {
        "username": "guest",
        "admin": False
    }

    raw = json.dumps(user).encode()
    xored = xor_data(raw, XOR_KEY)
    encoded = base64.b64encode(xored).decode()

    resp = make_response(render_template("index.html"))
    resp.set_cookie("session", encoded)

    return resp


@app.route("/admin")
def admin():
    cookie = request.cookies.get("session")

    if not cookie:
        return "No session found", 403

    try:
        decoded = base64.b64decode(cookie)
        raw = xor_data(decoded, XOR_KEY)
        user = json.loads(raw)
    except Exception:
        return "Invalid session", 403

    if user.get("admin") is True:
        return render_template("admin.html", user=user)

    return "Access denied", 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
