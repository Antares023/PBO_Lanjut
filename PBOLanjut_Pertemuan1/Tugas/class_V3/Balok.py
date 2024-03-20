class Segitiga :
    def __init__(self):
        self._panjang = None
        self._lebar = None
        self._tinggi = None

    @property
    def lebar(self):
        return self._lebar
    
    @lebar.setter
    def lebar(self, value):
        self._lebar = value

    @property
    def panjang(self):
        return self._panjang
    
    @panjang.setter
    def panjang(self, value):
        self._panjang = value

    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value

    def Volume(self):
        return self._lebar * self._panjang * self._tinggi
    
S = Segitiga()
P = input("Masukkan nilai panjang :")
L = input("Masukkan nilai lebar :")
T = input("Masukkan nilai tinggi :")

S.panjang = int(P)
S.lebar = int(L)
S.tinggi = int(T)

V = S.Volume()

print("="*35)
print("Panjang : ", P)
print("Lebar : ", L)
print("Tinggi : ", T)
print("Volume : ", V)
print("="*35)
