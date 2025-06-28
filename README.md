# 🎯 Targeted Laravel Brute Force Tool

Script Python ini digunakan untuk melakukan serangan **brute force** yang ditargetkan pada halaman login berbasis **Laravel**. Alat ini akan menguji daftar kata sandi (*wordlist*) untuk sebuah username tertentu dan **berhenti** jika menemukan kata sandi spesifik yang ditentukan.

⚠️ **Peringatan**: Alat ini hanya digunakan untuk tahap develop website untuk menguji keamanan dari login page tersebut.

---

## 🧩 Prasyarat

- Python 3.x telah terinstal.
- File `requirements.txt` dengan pustaka yang dibutuhkan.


## 🔧 Instalasi

```bash
# Arahkan ke direktori skrip dan file requirements.txt
cd /path/to/directory

# Instal pustaka yang diperlukan
pip install -r requirements.txt
````

---

## 🚀 Cara Penggunaan

Jalankan skrip dengan format berikut:

```bash
python brute_force_laravel.py [URL_LOGIN] [USERNAME] [PATH_KE_WORDLIST] --target-password [PASSWORD_TARGET]
```

### Argumen

| Argumen             | Deskripsi                                                             |
| ------------------- | --------------------------------------------------------------------- |
| `URL_LOGIN`         | URL lengkap dari halaman login target.                                |
| `USERNAME`          | Username yang akan diuji.                                             |
| `PATH_KE_WORDLIST`  | Path ke file wordlist (misal: `/usr/share/wordlists/rockyou.txt`).    |
| `--target-password` | *(Opsional)* Password target spesifik yang dicari. Default: `uwu123`. |

---

## 📌 Contoh Penggunaan

### 1. Mencari password target `password123`:

```bash
python brute_force_laravel.py http://website.com/login admin wordlist.txt --target-password password123
```

### 2. Menggunakan password default (`admin`):

```bash
python brute_force_laravel.py http://contoh-situs.net/masuk supervisor /path/to/rockyou.txt
```

---

## ⚖️ Disclaimer

> Skrip ini hanya untuk **pengujian sistem Anda sendiri** atau dalam konteks **audit keamanan dengan izin**. Penggunaan tanpa izin melanggar hukum dan etika profesional. Pengembang tidak bertanggung jawab atas penyalahgunaan alat ini.
