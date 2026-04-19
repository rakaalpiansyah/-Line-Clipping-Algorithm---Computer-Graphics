# 🖥️ Line Clipping Implementation: Cohen-Sutherland & Liang-Barsky

Proyek implementasi algoritma kliping garis (Line Clipping) untuk memenuhi tugas mata kuliah **Grafika Komputer** di Jurusan Informatika, UIN Sunan Gunung Djati Bandun.

---

## 🚀 Fitur Utama
* **Cohen-Sutherland Algorithm**: Implementasi berbasis pembagian wilayah menggunakan *4-bit region code*.
* **Liang-Barsky Algorithm**: Implementasi berbasis persamaan parametrik yang lebih efisien dibandingkan metode tradisional.
* **Interactive Visualization**: Perbandingan visual antara garis asli (shadow) dan hasil kliping menggunakan Matplotlib.
* **Professional Structure**: Arsitektur kode berbasis OOP yang bersih dan mudah dikembangkan.

---

## 🛠️ Prasyarat & Instalasi (Virtual Environment)

Sangat disarankan untuk menjalankan proyek ini di dalam **Virtual Environment (venv)** agar pustaka (*library*) proyek tidak mengganggu konfigurasi sistem global Anda.

### 1. Kloning atau Siapkan Folder Proyek
Pastikan Anda berada di direktori `Clipping_Project/` melalui terminal atau Command Prompt.

### 2. Buat dan Aktifkan Virtual Environment
Pilih instruksi yang sesuai dengan Sistem Operasi Anda:

* **Windows:**
    ```bash
    # Membuat venv
    python -m venv venv
    
    # Aktivasi venv
    venv\Scripts\activate
    ```

* **macOS / Linux:**
    ```bash
    # Membuat venv
    python -m venv venv
    
    # Aktivasi venv
    source venv/bin/activate
    ```
*Setelah aktif, Anda akan melihat tanda `(venv)` di sebelah kiri prompt terminal Anda.*

### 3. Instalasi Library
Gunakan pip untuk menginstal dependensi yang tercantum di `requirements.txt`:
```bash
pip install -r requirements.txt
