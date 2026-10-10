# Catatan Film Favorit

Program Python sederhana untuk menyimpan dan menganalisis daftar film favorit.

## Cara menjalankan

Buka terminal di folder proyek, lalu jalankan:

```powershell
python main.py
```

## Menjalankan pengujian

```powershell
python -m unittest film_app.testing -v
```

## File yang dibuat otomatis

- `film.txt`: data film.
- `laporan_film.txt`: hasil laporan yang dibuat melalui menu 3.

## Struktur proyek

- `main.py`: menu utama.
- `film_app/models.py`: class `Film` dan `KoleksiFilm`.
- `film_app/validasi.py`: validasi data dan exception khusus.
- `film_app/fileio.py`: fungsi baca dan tulis file.
- `film_app/processing.py`: perhitungan dan analisis film.
- `film_app/testing.py`: pengujian menggunakan `unittest`.
- `film_app/__init__.py`: inisialisasi package.
