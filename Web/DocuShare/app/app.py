import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__, static_folder="static", template_folder="templates")

BASE_DIR = os.path.dirname(__file__)
STORAGE_ROOT = os.path.join(BASE_DIR, "storage")

# Map numeric owner_id -> username (match your storage folder names)
USER_ID_MAP = {
    1: "ammar",
    2: "abdesattar"   # -> matches your app/storage folder
}

def _safe_file_path(user_dir, filename):
    candidate = os.path.abspath(os.path.normpath(os.path.join(user_dir, filename)))
    user_dir_abs = os.path.abspath(user_dir)
    if not (candidate == user_dir_abs or candidate.startswith(user_dir_abs + os.sep)):
        return None
    return candidate

def levenshtein(a: str, b: str) -> int:
    """Compute Levenshtein distance (iterative DP)."""
    if a == b:
        return 0
    la, lb = len(a), len(b)
    if la == 0:
        return lb
    if lb == 0:
        return la
    # ensure smaller dimension for memory: use two rows
    prev = list(range(lb + 1))
    cur = [0] * (lb + 1)
    for i in range(1, la + 1):
        cur[0] = i
        ai = a[i - 1]
        for j in range(1, lb + 1):
            cost = 0 if ai == b[j - 1] else 1
            cur[j] = min(prev[j] + 1,        # deletion
                         cur[j - 1] + 1,     # insertion
                         prev[j - 1] + cost) # substitution
        prev, cur = cur, prev
    return prev[lb]

def resolve_storage_username(requested_name: str) -> str:
    """
    Find the best matching directory under STORAGE_ROOT for requested_name.
    Strategy:
      - exact match
      - case-insensitive exact
      - pick the entry with smallest Levenshtein distance if distance <= threshold
      - fallback to requested_name
    """
    if not os.path.isdir(STORAGE_ROOT):
        return requested_name

    # exact
    cand = os.path.join(STORAGE_ROOT, requested_name)
    if os.path.isdir(cand):
        return requested_name

    # case-insensitive match
    entries = [e for e in os.listdir(STORAGE_ROOT) if os.path.isdir(os.path.join(STORAGE_ROOT, e))]
    for entry in entries:
        if entry.lower() == requested_name.lower():
            return entry

    # compute levenshtein distances and pick minimal one if close enough
    best = None
    best_dist = None
    for entry in entries:
        d = levenshtein(entry.lower(), requested_name.lower())
        if best is None or d < best_dist:
            best = entry
            best_dist = d

    # choose threshold: allow small typos; threshold = 3 (empiric)
    if best is not None and best_dist is not None and best_dist <= 3:
        return best

    # fallback
    return requested_name

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip() or "Visitor"
        return render_template("contact.html", submitted=True, name=name)
    return render_template("contact.html", submitted=False)

# Profile page — exact content you provided
@app.route("/profile")
def profile():
    dummy = {
        "username": "Lmouldi",
        "full_name": "Lmouldi l3ataar",
        "email": "lmouldi@l3ataar.com",
        "role": "Member",
        "joined": "2025",
        "location": "Unknown",
        "bio": "Rabbi y3inek 3am lmouldi (lawej mli7)"
    }
    return render_template("profile.html", profile=dummy)

@app.route("/robots.txt")
def robots():
    robots_path = os.path.join(app.static_folder, "robots.txt")
    if os.path.isfile(robots_path):
        return send_file(robots_path, mimetype="text/plain")
    return "User-agent: *\nDisallow:\n# Users:\n# ammar\n# abdesattar\n", 200, {"Content-Type": "text/plain"}

@app.route("/ammar")
def ammar_files():
    requested = "ammar"
    real = resolve_storage_username(requested)
    user_dir = os.path.join(STORAGE_ROOT, real)
    files = []
    if os.path.isdir(user_dir):
        for root, dirs, filenames in os.walk(user_dir):
            for fn in filenames:
                rel = os.path.relpath(os.path.join(root, fn), user_dir)
                files.append(rel.replace("\\", "/"))
    return render_template("user_files.html", requested=requested, username=real, files=sorted(files))

@app.route("/abdessattar")
def abdessattar_files():
    requested = "abdessattar"
    real = resolve_storage_username(requested)
    user_dir = os.path.join(STORAGE_ROOT, real)
    files = []
    if os.path.isdir(user_dir):
        for root, dirs, filenames in os.walk(user_dir):
            for fn in filenames:
                rel = os.path.relpath(os.path.join(root, fn), user_dir)
                files.append(rel.replace("\\", "/"))
    return render_template("user_files.html", requested=requested, username=real, files=sorted(files))

@app.route("/view/<username>/<path:filename>")
def view_file(username, filename):
    real = resolve_storage_username(username)
    user_dir = os.path.join(STORAGE_ROOT, real)
    safe = _safe_file_path(user_dir, filename)
    if not safe or not os.path.isfile(safe):
        return render_template("file_viewer.html", username=real, filename=filename, content=None, missing=True)
    try:
        with open(safe, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception:
        content = None
    return render_template("file_viewer.html", username=real, filename=filename, content=content, missing=False)

@app.route("/files/<username>/<path:filename>")
def get_file_by_username(username, filename):
    real = resolve_storage_username(username)
    user_dir = os.path.join(STORAGE_ROOT, real)
    safe = _safe_file_path(user_dir, filename)
    if not safe:
        return "Invalid path", 400
    if not os.path.isfile(safe):
        return "Not found", 404
    return send_file(safe, as_attachment=False)

@app.route("/files/id/<int:owner_id>/<path:filename>")
def get_file_by_id(owner_id, filename):
    username = USER_ID_MAP.get(owner_id)
    if not username:
        return "User not found", 404
    real = resolve_storage_username(username)
    user_dir = os.path.join(STORAGE_ROOT, real)
    safe = _safe_file_path(user_dir, filename)
    if not safe:
        return "Invalid path", 400
    if not os.path.isfile(safe):
        return "Not found", 404
    return send_file(safe, as_attachment=False)

if __name__ == "__main__":
    os.makedirs(STORAGE_ROOT, exist_ok=True)
    app.run(host="0.0.0.0", port=4001, debug=False)
