class Lingkaran :
    def __init__ (self):
        self.r = None
        self.pi = None
        self.luas = None

    def Luas(self, r, pi):
        self.r = r
        self.pi = 3.14
        self.luas = self.pi * self.r**2
        return self.luas
    
P = Lingkaran()
r = input("Masukkan Nilai r :")
pi = 3.14
luas = P.Luas(int(r), int(pi))

print("Jari-jari :", r)
print("pi :", 3.14)
print("Luas :", luas)