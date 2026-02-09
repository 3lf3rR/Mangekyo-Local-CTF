from flask import Flask, request, render_template, make_response
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "naruto"
@app.route('/')
def index():
    token = request.cookies.get('auth_token')
    if not token:
        payload = {
            "user": "guest",
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        resp = make_response(render_template('index.html', 
                                           message="Only 'admin' can access the secret files.", 
                                           username="guest"))
        resp.set_cookie('auth_token', token)
        return resp

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if data.get("user") == "admin":
            with open("flag.txt", "r") as f:
                flag_content = f.read()
            return render_template('index.html', 
                                 message="Welcome back, Authorized Administrator.", 
                                 username="admin", 
                                 flag=flag_content)
        else:
            return render_template('index.html', 
                                 message="Access Denied: Standard user profile detected.", 
                                 username=data.get("user"))
    except Exception:
        return "Invalid Session", 401
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)