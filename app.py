@app.route("/info", methods=["GET"])
def info():
    """Menampilkan halaman informasi tambahan aplikasi."""
    return "<h1>Halaman Informasi</h1><p>Route baru berhasil ditambahkan dan ter-deploy otomatis.</p>"