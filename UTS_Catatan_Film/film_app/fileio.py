from .processing import buat_film


# Membuat file baru jika belum tersedia
def buat_file(nama_file):
    try:
        with open(nama_file, "x", encoding="utf-8") as file:
            file.write("")

    except FileExistsError:
        # File sudah ada, jadi tidak perlu dibuat ulang
        pass


# Membaca film dari file
def baca_film(nama_file):
    daftar_film = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                if not baris.strip():
                    continue

                try:
                    bagian = baris.strip().split(";")

                    if len(bagian) != 4:
                        raise ValueError("Format data tidak sesuai.")

                    judul, genre, tahun, rating = bagian

                    film = buat_film(
                        judul=judul,
                        genre=genre,
                        tahun=tahun,
                        rating=rating
                    )

                    daftar_film.append(film)

                except (ValueError, TypeError) as error:
                    # Melewati baris yang datanya tidak valid
                    print(f"Baris {nomor} dilewati: {error}")

    except FileNotFoundError:
        print(f"File {nama_file} belum tersedia.")

    return daftar_film


# Menambahkan satu film tanpa menghapus data lama
def tambah_file(nama_file, film):
    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(film.ke_baris() + "\n")


# Menulis laporan dan mengganti isi laporan lama
def tulis_laporan(nama_file, isi):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(isi)
