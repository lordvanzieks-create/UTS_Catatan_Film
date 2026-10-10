import unittest

from .processing import (
    buat_film,
    hitung_rata_rata,
    analisis_film
)

from .validasi import DataFilmError


class TestCatatanFilm(unittest.TestCase):

    # Menyiapkan data untuk setiap pengujian
    def setUp(self):
        self.film = [
            buat_film(
                judul="Naruto",
                genre="Anime",
                tahun=2002,
                rating=9
            ),
            buat_film(
                judul="One Piece",
                genre="Anime",
                tahun=1999,
                rating=8
            ),
            buat_film(
                judul="Toy Story",
                genre="Animasi",
                tahun=1995,
                rating=7
            )
        ]

    # Menguji perhitungan rata-rata
    def test_rata_rata(self):
        hasil = hitung_rata_rata(9, 8, 7)
        self.assertEqual(hasil, 8)

    # Menguji jumlah film
    def test_jumlah_film(self):
        hasil = analisis_film(self.film)
        self.assertEqual(hasil["jumlah"], 3)

    # Menguji film dengan rating tertinggi
    def test_rating_tertinggi(self):
        hasil = analisis_film(self.film)
        self.assertEqual(
            hasil["film_tertinggi"].judul,
            "Naruto"
        )

    # Menguji rekomendasi berdasarkan rating
    def test_rekomendasi(self):
        hasil = analisis_film(
            self.film,
            batas_rating=8
        )

        self.assertEqual(
            [film.judul for film in hasil["rekomendasi"]],
            ["Naruto", "One Piece"]
        )

    # Menguji penolakan rating di atas 10
    def test_rating_tidak_valid(self):
        with self.assertRaises(DataFilmError):
            buat_film(
                judul="Film Salah",
                genre="Drama",
                tahun=2020,
                rating=11
            )

    # Menguji analisis saat daftar film kosong
    def test_daftar_kosong(self):
        hasil = analisis_film([])

        self.assertEqual(hasil["jumlah"], 0)
        self.assertEqual(hasil["rata_rata"], 0)


if __name__ == "__main__":
    unittest.main()
