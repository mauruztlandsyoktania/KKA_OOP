class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

# Class Mage adalah anak dari class Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # Memanggil constructor milik Parent (Hero)
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    # Mage punya skill khusus
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)  # Damage 2x
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# -- Main Program Baru --
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)        # Serangan biasa (warisan dari Hero)
eudora.skill_fireball(balmond)  # Skill khusus Mage


class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat Private
        self.__hp = hp_awal

    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: Cara resmi mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        # Pakai getter & setter agar aman
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# -- Uji Coba --
hero1 = Hero("Layla", 100)

# hero1.__hp = 9999   # ❌ Tidak mengubah HP asli
# print(hero1.__hp)   # ❌ Error

hero1.set_hp(-50)     # Coba set negatif
print(hero1.get_hp()) # Output: 0


from abc import ABC, abstractmethod
# 1. Interface / Abstract Class
# Ini adalah KONTRAK. Semua turunan wajib punya method di bawah ini.
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# 2. Implementasi pada Class Konkret
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    # Wajib implementasi method abstract
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
# unit = GameUnit()  # ❌ ERROR (abstract class tidak bisa diinstansiasi)

h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()


# Parent Class
class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


# Child Class 1
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")


# Child Class 2
class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


# Child Class 3
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


# -- Penerapan Polymorphism --
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

print("--- PERANG DIMULAI ---")

# Satu perintah loop, respon berbeda (Polymorphism)
for pahlawan in pasukan:
    pahlawan.serang()



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