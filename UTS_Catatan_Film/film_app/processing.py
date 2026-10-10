from .models import Film
from .validasi import validasi_film


# Membuat film menggunakan **kwargs
def buat_film(**data):
    atribut = {"judul", "genre", "tahun", "rating"}

    if not atribut.issubset(data):
        raise ValueError("Data film belum lengkap.")

    data_valid = validasi_film(
        data["judul"],
        data["genre"],
        data["tahun"],
        data["rating"]
    )

    return Film(**data_valid)


# Menghitung rata-rata dengan *args
def hitung_rata_rata(*rating):
    if not rating:
        raise ValueError("Rating belum tersedia.")

    return sum(rating) / len(rating)


# Menganalisis daftar film
def analisis_film(daftar_film, batas_rating=8):
    if not daftar_film:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "film_tertinggi": None,
            "rekomendasi": []
        }

    rata_rata = hitung_rata_rata(
        *(film.rating for film in daftar_film)
    )

    # Lambda digunakan untuk menentukan rating tertinggi
    tertinggi = max(
        daftar_film,
        key=lambda film: film.rating
    )

    # Mengurutkan film yang ratingnya memenuhi batas
    rekomendasi = sorted(
        [film for film in daftar_film if film.rating >= batas_rating],
        key=lambda film: film.rating,
        reverse=True
    )

    return {
        "jumlah": len(daftar_film),
        "rata_rata": rata_rata,
        "film_tertinggi": tertinggi,
        "rekomendasi": rekomendasi
    }


# Membuat teks laporan
def buat_laporan(hasil):
    baris = [
        "LAPORAN CATATAN FILM",
        "=" * 25,
        f"Jumlah film: {hasil['jumlah']}",
        f"Rata-rata rating: {hasil['rata_rata']:.2f}"
    ]

    if hasil["film_tertinggi"] is not None:
        film = hasil["film_tertinggi"]
        baris.append(
            f"Rating tertinggi: {film.judul} ({film.rating:.1f})"
        )

    baris.append("")
    baris.append("DAFTAR REKOMENDASI")

    if hasil["rekomendasi"]:
        for film in hasil["rekomendasi"]:
            baris.append(
                f"- {film.judul} | {film.genre} | "
                f"{film.tahun} | Rating {film.rating:.1f}"
            )
    else:
        baris.append("Belum ada film yang memenuhi batas rating.")

    return "\n".join(baris)
