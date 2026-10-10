from pathlib import Path

from film_app.models import KoleksiFilm
from film_app.processing import (
    buat_film,
    analisis_film,
    buat_laporan
)
from film_app.fileio import (
    buat_file,
    baca_film,
    tambah_file,
    tulis_laporan
)


# Menentukan lokasi file di folder proyek
FOLDER = Path(__file__).resolve().parent
FILE_DATA = FOLDER / "film.txt"
FILE_LAPORAN = FOLDER / "laporan_film.txt"


# Menampilkan seluruh film
def tampilkan_film(daftar_film):
    if not daftar_film:
        print("Belum ada film.")
        return

    for film in daftar_film:
        print(
            f"{film.judul} | {film.genre} | "
            f"{film.tahun} | Rating: {film.rating}"
        )


# Menambahkan film baru
def menu_tambah():
    try:
        judul = input("Judul film: ")
        genre = input("Genre: ")
        tahun = input("Tahun rilis: ")
        rating = input("Rating (0-10): ")

        film = buat_film(
            judul=judul,
            genre=genre,
            tahun=tahun,
            rating=rating
        )

        koleksi = KoleksiFilm(baca_film(FILE_DATA))
        koleksi.tambah(film)

        tambah_file(FILE_DATA, film)
        print("Film berhasil ditambahkan.")

    except (ValueError, OSError) as error:
        print(f"Gagal menambahkan film: {error}")


# Membuat dan menampilkan laporan
def menu_laporan():
    daftar_film = baca_film(FILE_DATA)

    hasil = analisis_film(
        daftar_film,
        batas_rating=8
    )

    laporan = buat_laporan(hasil)
    tulis_laporan(FILE_LAPORAN, laporan)

    print("\n" + laporan)
    print(f"\nLaporan tersimpan di: {FILE_LAPORAN}")


# Menu utama
def main():
    buat_file(FILE_DATA)

    while True:
        print("\n=== CATATAN FILM FAVORIT ===")
        print("1. Lihat daftar film")
        print("2. Tambah film")
        print("3. Buat laporan")
        print("4. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_film(baca_film(FILE_DATA))

        elif pilihan == "2":
            menu_tambah()

        elif pilihan == "3":
            menu_laporan()

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


# Hanya menjalankan menu ketika file dieksekusi langsung
if __name__ == "__main__":
    main()
