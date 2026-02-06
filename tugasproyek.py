from abc import ABC, abstractmethod

# ================= ABSTRACT CLASS =================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = 0

    # ENCAPSULATION
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def _get_harga_dasar(self):
        return self.__harga_dasar

    # ABSTRACT METHODS
    @abstractmethod
    def tampilkan_detail(self, jumlah, nomor):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ================= LAPTOP =================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self, jumlah, nomor):
        pajak = self._get_harga_dasar() * 0.10
        subtotal = self.hitung_harga_total(jumlah)

        print(f"{nomor}. [LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {self._get_harga_dasar():,.0f} | Pajak(10%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}\n")

    def hitung_harga_total(self, jumlah):
        return (self._get_harga_dasar() * 1.10) * jumlah


# ================= SMARTPHONE =================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self, jumlah, nomor):
        pajak = self._get_harga_dasar() * 0.05
        subtotal = self.hitung_harga_total(jumlah)

        print(f"{nomor}. [SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {self._get_harga_dasar():,.0f} | Pajak(5%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}\n")

    def hitung_harga_total(self, jumlah):
        return (self._get_harga_dasar() * 1.05) * jumlah


# ================= TRANSAKSI =================
def proses_transaksi(keranjang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, (barang, jumlah) in enumerate(keranjang, start=1):
        barang.tampilkan_detail(jumlah, i)
        total += barang.hitung_harga_total(jumlah)

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")


# ================= MAIN =================
if __name__ == "__main__":
    print("Plaintext --- SETUP DATA ---")

    laptop = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
    hp = Smartphone("iPhone 13", 15_000_000, "12MP")

    laptop.tambah_stok(10)
    hp.tambah_stok(-5)
    hp.tambah_stok(20)

    keranjang = [
        (laptop, 2),
        (hp, 1)
    ]

    proses_transaksi(keranjang)