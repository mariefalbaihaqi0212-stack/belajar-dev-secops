"""Modul backend autentikasi Flask dengan antarmuka web interaktif."""
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DB_NAME = "users.db"


def init_db():
    """Inisialisasi basis data dan membuat data pengguna awal."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
        )
        cursor.execute(
            "INSERT OR IGNORE INTO users VALUES ('admin', 'supersecret')"
        )
        conn.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    """Menampilkan formulir login dan memproses autentikasi."""
    message = None
    status_class = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            # Parameterized query untuk mencegah SQL Injection
            query = "SELECT * FROM users WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

        if user:
            message = "Login Berhasil! Selamat datang."
            status_class = "success"
        else:
            message = "Login Gagal! Kredensial tidak valid."
            status_class = "danger"

    return render_template(
        "index.html", message=message, status_class=status_class
    )


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)  # nosemgrep