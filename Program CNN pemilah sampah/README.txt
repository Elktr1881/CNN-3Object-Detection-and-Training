Langkah-langkah ambil sample data :
> Buka Program Ambil Data.py
> Atur direktori penympanan gambar (line 9)
contoh : #save_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\train\Kaleng\kaleng'
*Beri nama folder sesuai nama objek deteksi
*Simpan gambar training pada folder train >> gambar training terdiri dari banyak gambar min.50 gambar,semakin banyak = semakin akurat
*Simpan gambar validasi pada folder falidation >> gambar falidasi berfungsi untuk matching data, mencakup semua variasi jenis training, semakun berfariasi = semakin akurat
> jalankan program
> letakkan objek yang akan di ambil di depan kamera
> tekan tombol s untuk menympan, ambil sampai kuantitas yang diiginkan

Langkah-langkah membuat datasheet :
> Buka Program Learning.py
> Ubah direktori seusai penympanan data training dan validation (line 25-26)
> Ubah direktori untuk menyimpan datasheet (line 104)/paling bawah
> Jalankan program..
> tunggu proses selesai

Langkah-langkah menjealankan program inti :
> Buka program Deteksi(inti).py
> Ubah direktori datasheet sesuai penimpanan datasheet (line 6)
> Jalankan program..
> Selesai



