import os
import ipaddress
from flask import Flask, request, render_template, redirect, url_for, flash
import requests
from urllib.parse import urlparse, unquote

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-only-secret")

MAX_PREVIEW_CHARS = 2000
ONLY_ALLOWED_LOOPBACK_HOST = "2130706433"


def _is_ipv4ish(host: str) -> bool:
    parts = host.split(".")
    if not (1 <= len(parts) <= 4):
        return False
    return all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)


def _normalize_ipv4(host: str) -> str | None:
    if not _is_ipv4ish(host):
        return None
    parts = host.split(".")
    parts = parts + ["0"] * (4 - len(parts))
    return ".".join(str(int(p)) for p in parts)


def _blocked_host(host: str) -> bool:
    if not host:
        return True

    h = host.lower()

    if h == ONLY_ALLOWED_LOOPBACK_HOST:
        return False

    if h in ("localhost", "localhost.", "ip6-localhost"):
        return True

    if h.isdigit():
        return True

    if _is_ipv4ish(h):
        norm = _normalize_ipv4(h)
        if norm:
            try:
                ip = ipaddress.ip_address(norm)
                if ip.is_loopback:
                    return True
            except ValueError:
                return True
        return False

    try:
        ip6 = ipaddress.ip_address(h)
        if ip6.is_loopback:
            return True
        if isinstance(ip6, ipaddress.IPv6Address) and ip6.ipv4_mapped:
            if ip6.ipv4_mapped.is_loopback:
                return True
    except ValueError:
        pass

    if h.startswith("::ffff:127."):
        return True

    if "@" in h:
        return True

    if h.startswith("0x") or any(c in h for c in "abcdef"):
        return True

    return False


def policy_block(url: str) -> bool:
    u = unquote((url or "").strip())
    p = urlparse(u)
    if p.scheme not in ("http", "https"):
        return True
    return _blocked_host(p.hostname or "")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = (request.form.get("url") or "").strip()
        return redirect(url_for("preview", url=url))
    return render_template("index.html")


@app.route("/preview")
def preview():
    url = (request.args.get("url") or "").strip()
    if not url:
        flash("Please enter a URL.")
        return redirect(url_for("index"))

    if policy_block(url):
        flash("That destination is blocked by policy.")
        return redirect(url_for("index"))

    try:
        r = requests.get(
            url,
            timeout=2,
            allow_redirects=True,
            headers={"User-Agent": "IntraPreviewBot/1.0"},
        )
        return render_template(
            "preview.html",
            url=url,
            status=r.status_code,
            content_type=r.headers.get("Content-Type", "unknown"),
            body=(r.text or "")[:MAX_PREVIEW_CHARS],
        )
    except requests.RequestException:
        return render_template(
            "preview.html",
            url=url,
            status="error",
            content_type="-",
            body="Request failed.",
        )


@app.route("/internal/flag")
def internal_flag():
    if request.remote_addr not in ("127.0.0.1", "::1"):
        return "Forbidden", 403
    return os.environ.get("FLAG", "Securinets{FAKE_FLAG}") + "\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
