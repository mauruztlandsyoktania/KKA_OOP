## Tugas Analisis 1: • Apa yang terjadi jika kamu mengubah hero1.
# hp menjadi 500 setelah baris hero1 = Hero...? Coba lakukan print(hero1.hp).

## Jawab: Nilai hp dari hero1 akan berubah menjadi 500, sehingga ketika diprint, outputnya akan 500.

##Tugas Analisis 2:
#Perhatikan parameter lawan pada method serang. Parameter tersebut
#menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini
#penting?

##Jawaban: Karena dengan menerima objek utuh, kita bisa mengakses semua atribut dan method dari objek lawan,
#bukan hanya nama. Misalnya, kita bisa memeriksa hp lawan, atau memanggil method lain dari objek lawan.

##Tugas Analisis 3:
#• Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan
#• Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora
# (eudora.info())? Mengapa error tersebut mengatakan Mage object has no
# attribute 'name', padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?
# • Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke class Induk!

## jawaban: Error yang muncul adalah Mage object has no attribute 'name' karena constructor 
# Hero tidak dijalankan. Fungsi super() berfungsi memanggil constructor class Induk agar 
# atribut seperti name dan hp dimiliki oleh class Anak.

## Tugas Analisis 4:
#1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling bawah (luar class): 
# print(f"Mencoba akses paksa: {hero1._Hero__hp}")
# Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan 
# temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling) 
# dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik. 
#2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya 
# hanya self.__hp = nilai_baru.
# Pertanyaan: Kemudian lakukan hero1.set_hp(-100).
# Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method
# Setter sangat penting untuk menjaga integritas data dalam game!

##jawaban:
#1. Nilai HP muncul ketika mengakses hero1._Hero__hp karena Python menggunakan
# konsep Name Mangling untuk atribut private. Namun, mengakses atribut private
# secara langsung tidak dianjurkan karena melanggar prinsip enkapsulasi dan dapat menyebabkan inkonsistensi data.
#2. Jika logika validasi dihapus dan kita melakukan hero1.set_hp(-100), maka HP
# hero1 akan menjadi -100. Hal ini menunjukkan pentingnya method Setter untuk
# menjaga integritas data, karena tanpa validasi, data dapat menjadi tidak 
# valid atau merusak logika permainan.

##Tugas Analisis 5:
#1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh 
# blok method def serang(self, target):. Jalankan programnya.
# Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti
# pesan error Can't instantiate abstract class Hero with abstract method...?
# Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?
#2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit().
# Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
# Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

##jawaban:
#Interface memastikan aturan dipatuhi. Class abstrak tidak dibuat untuk dipakai langsung, 
# tetapi sebagai dasar bagi class lain.

##Tugas Analisis 6
#1. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf 
# pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class baru bernama Healer(Hero).
# Isi method serang milik Healer dengan: print(f"{self.name} tidak
# menyerang, tapi menyembuhkan teman!").Masukkan objek Healer ke dalam list pasukan.
# Pertanyaan: Apakah program berjalan lancar?
# Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer
# ketika harus mengupdate game dengan karakter baru di masa depan?
#2. Konsistensi Penamaan: Ubah nama method serang pada class Archer
# menjadi tembak_panah. Jalankan program.
# Pertanyaan: Apa yang terjadi?
# Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan
# berbagai Child Class harus persis sama?
