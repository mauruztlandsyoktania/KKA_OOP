class Akunbank:
    def __init__(self, saldo):
        self.__saldo = saldo # Private attribute

        def cek_saldo(self):
            return self.__saldo
        
        def setor(self, jumlah):
            if jumlah > 0:
                self.__saldo += jumlah
            else:
                print("Jumlah setor harus positif.")

                def tarik(self, jumlah):
                    if jumlah > 0 and jumlah <= self.__saldo:
                        self.__saldo -= jumlah
                    else:
                        print("Jumlah tarik atau saldo tidak mencukupi. ")

rekening = Akunbank(1000)
rekening.stor(500)
rekening.tarik(2000)
#print(rekening.cek_saldo()) # Output: 1500
# print(rekening._saldo)  # Tpi akan EROR Tidak bisa akses langsung