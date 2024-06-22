# Trcak

Skrip Python untuk mencari informasi nomor telepon menggunakan Twilio API.

## Persyaratan

- Python 3.x
- Twilio SDK (`twilio`)
- Git

## Cara Menggunakan

### Termux

1. **Instal Git dan Python di Termux**
   ```sh
   pkg update
   pkg install git
   pkg install python
Clone Repository dari GitHub

sh
Salin kode
git clone https://github.com/xwbyy/trcak.git
cd trcak
Instal Twilio SDK

sh
Salin kode
pip install twilio
Jalankan Skrip

sh
Salin kode
python lookup_phone.py
Windows
Instal Git dan Python di Windows

Unduh dan instal Git dari https://git-scm.com/.
Unduh dan instal Python dari https://www.python.org/.
Clone Repository dari GitHub

Buka Command Prompt atau PowerShell.
Jalankan perintah berikut untuk meng-clone repository:
sh
Salin kode
git clone https://github.com/xwbyy/trcak.git
cd trcak
Instal Twilio SDK

sh
Salin kode
pip install twilio
Jalankan Skrip

sh
Salin kode
python lookup_phone.py
Mengubah Nomor Telepon
Jika Anda ingin mengubah nomor telepon yang akan dicari informasinya, edit file lookup_phone.py dan ganti nilai variabel phone_number:

python
Salin kode
phone_number = '+1234567890'  # Ganti dengan nomor telepon yang Anda cari
Mengunggah Perubahan ke GitHub
Jika Anda membuat perubahan pada skrip dan ingin mengunggahnya kembali ke GitHub, lakukan langkah-langkah berikut:

Tambahkan Perubahan dan Commit

sh
Salin kode
git add lookup_phone.py
git commit -m "Updated phone number"
Unggah ke Repository

sh
Salin kode
git push origin master
Lisensi
Skrip ini dilisensikan di bawah MIT License.

go
Salin kode

Salin dan tempel isi ini ke file `README.md` di root directory proyek Anda di GitHub. Jika ada pertanyaan lebih lanjut atau bantuan tambahan, jangan ragu untuk bertanya!




