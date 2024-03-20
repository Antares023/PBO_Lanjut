class LabaBulanan :
    def __init__(self):
        self._jual = None
        self._beli = None
        self._bulan = None

    @property
    def beli(self):
        return self._beli
    
    @beli.setter
    def beli(self, value):
        self._beli = value

    @property
    def jual(self):
        return self._jual
    
    @jual.setter
    def jual(self, value):
        self._jual = value

    @property
    def bulan(self):
        return self._bulan
    
    @bulan.setter
    def bulan(self, value):
        self._bulan = value

    def Hasil(self):
        return (self._jual - self._beli) * self._bulan
    
L = LabaBulanan()
J = input("Masukkan nilai jual :")
B = input("Masukkan nilai beli :")
H = input("Masukkan nilai bulan(dalam hari) :")

L.jual = int(J)
L.beli = int(B)
L.bulan = int(H)

T = L.Hasil()

print("="*35)
print("jual : ", J)
print("beli : ", B)
print("bulan : ", H, "hari")
print("Laba Yang Didapat : ", T)
print("="*35)
