"""Modul sederhana untuk demonstrasi Pylint quality gate."""
def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang.
    Args:
        panjang: Panjang sisi persegi panjang.
        lebar: Lebar sisi persegi panjang.
    Returns:
        Hasil perkalian panjang dan lebar.
    """
    return panjang * lebar
def main():
    """Fungsi utama program."""
    hasil = hitung_luas_persegi_panjang(5, 3)
    print(f"Luas persegi panjang: {hasil}")
if __name__ == "__main__":
    main()