from .validasi import DataFilmError


# Menyimpan informasi satu film
class Film:
    def __init__(self, judul, genre, tahun, rating):
        # Memastikan tahun yang diterima sudah benar
        assert isinstance(tahun, int) and tahun > 0

        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = float(rating)

    # Mengubah informasi film menjadi satu baris teks
    def ke_baris(self):
        return f"{self.judul};{self.genre};{self.tahun};{self.rating}"


# Mengelola kumpulan film
class KoleksiFilm:
    def __init__(self, daftar_film=None):
        self.daftar_film = list(daftar_film) if daftar_film else []

    # Menambahkan film dan menolak judul yang sama
    def tambah(self, film):
        for item in self.daftar_film:
            if item.judul.casefold() == film.judul.casefold():
                raise DataFilmError("Judul film sudah terdaftar.")

        self.daftar_film.append(film)
