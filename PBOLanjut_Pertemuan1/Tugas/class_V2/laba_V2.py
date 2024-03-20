class Persegi :
    def __init__ (self):
        self.jual = None
        self.beli = None
        self.laba = None

    def Laba(self, jual, beli):
        self.jual = jual
        self.beli = beli
        self.laba = self.jual - self.beli
        return self.laba
    
P = Persegi()
jual = input("Masukkan Harga jual :")
beli = input("Masukkan Harga beli :")
laba = P.Laba(int(jual), int(beli))

print("jual :", jual)
print("beli :", beli)
print("laba :", laba)