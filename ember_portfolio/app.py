import os
import re
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-local-development-key")

# Locally, the database is stored in the project folder.
# On Render, set DB_PATH=/var/data/portfolio.db and attach a persistent disk.
DB_PATH = os.environ.get("DB_PATH", str(Path(__file__).with_name("portfolio.db")))

def get_connection():
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all fields.", "error")
        return redirect(url_for("home") + "#contact")

    if len(name) > 80 or len(email) > 254 or len(message) > 2000:
        flash("One or more fields are too long. Please shorten your message.", "error")
        return redirect(url_for("home") + "#contact")

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("home") + "#contact")

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )

    flash("Thanks! Your message has been saved.", "success")
    return redirect(url_for("home") + "#contact")

@app.route("/health")
def health():
    return {"status": "ok"}

create_database()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=True)
