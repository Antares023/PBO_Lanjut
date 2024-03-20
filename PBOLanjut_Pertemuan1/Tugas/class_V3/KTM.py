class KTM :
    def __init__(self):
        self._nama = None
        self._nim = None
        self._prodi = None

    @property
    def nim(self):
        return self._nim
    
    @nim.setter
    def nim(self, value):
        self._nim = value

    @property
    def nama(self):
        return self._nama
    
    @nama.setter
    def nama(self, value):
        self._nama = value

    @property
    def prodi(self):
        return self._prodi
    
    @prodi.setter
    def prodi(self, value):
        self._prodi = value
    
S = KTM()
P = input("Masukkan nama :")
L = input("Masukkan nim :")
T = input("Masukkan prodi :")

S.nama = str(P)
S.nim = str(L)
S.prodi = str(T)

print("="*31)
print("="*4, "KARTU TANDA MAHASISWA", "="*4)
print("Nama : ", P)
print("NIM : ", L)
print("Prodi : ", T)
print("="*31)
