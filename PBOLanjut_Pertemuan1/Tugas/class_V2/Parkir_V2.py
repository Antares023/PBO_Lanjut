class Parkir :
    def __init__ (self):
        self.kendaraan = None
        self.platNomor = None

    def Data(self, kendaraan, platNomor):
        self.kendaraan = kendaraan
        self.platNomor = platNomor
        return self.data
    
P = Parkir()
kendaraan = input("Masukkan Jenis kendaraan :")
platNomor = input("Masukkan Plat Nomor :")

print("="*21)
print("="*4, "DATA PARKIR", "="*4)
print("Kendaraan :", kendaraan)
print("Plat Nomor :", platNomor)
print("="*21)