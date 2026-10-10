# Exception khusus untuk data film yang tidak valid
class DataFilmError(ValueError):
    pass


# Memeriksa data film
def validasi_film(judul, genre, tahun, rating):
    judul = str(judul).strip()
    genre = str(genre).strip()

    if not judul or not genre:
        raise DataFilmError("Judul dan genre tidak boleh kosong.")

    if ";" in judul or ";" in genre:
        raise DataFilmError("Judul dan genre tidak boleh mengandung titik koma.")

    try:
        tahun = int(tahun)
        rating = float(rating)
    except (ValueError, TypeError) as error:
        raise DataFilmError("Tahun dan rating harus berupa angka.") from error

    if tahun <= 0:
        raise DataFilmError("Tahun harus lebih dari nol.")

    if rating < 0 or rating > 10:
        raise DataFilmError("Rating harus berada antara 0 sampai 10.")

    return {
        "judul": judul,
        "genre": genre,
        "tahun": tahun,
        "rating": rating
    }
