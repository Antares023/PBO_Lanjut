class Segitiga :
    def __init__(self):
        self._tinggi = None
        self._alas = None

    @property
    def alas(self):
        return self._alas
    
    @alas.setter
    def alas(self, value):
        self._alas = value

    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value

    def Luas(self):
        return 0.5 * self._alas * self._tinggi
    
S = Segitiga()
A = input("Masukkan nilai alas :")
T = input("Masukkan nilai tinggi :")

S.alas = int(A)
S.tinggi = int(T)

L = S.Luas()

print("Alas", A)
print("Tinggi", T)
print("Luas", L)
