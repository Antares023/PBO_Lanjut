class Laba:
    def __init__(self, jual, beli, bulan):
        self.__jual = 0
        self.__beli = 0
        self.__bulan = 0
        self.__setJual(jual)
        self.__setBeli(beli)
        self.__setBulan(bulan)
        
    def getJual(self):
        return self.__jual
    
    def getBeli(self):
        return self.__beli
    
    def getBulan(self):
        return self.__bulan
    
    def __setJual(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__jual = nilai
    
    def __setBeli(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__beli = nilai
        
    def __setBulan(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__bulan = nilai
        
    def LabaHarian(self):
        L = self.__jual - self.__beli
        return L
    
    def LabaBulanan(self):
        K = (2* self.__jual) + (2* self.__beli)
        return K
    
try:
    jual = int(input("Masukkan harga jual : "))
    beli = int(input("Masukkan harga beli : "))
    bulan = int(input("Masukkan jumlah bulan dalam hari : "))
except ValueError:
    print("Masukkan hanya angka saja!")
else :
    P = Laba(jual, beli, bulan)
    L = P.LabaHarian()
    K = P.LabaBulanan()
    print("Harga Jual : ", P.getJual())
    print("Harga Beli : ", P.getBeli())
    print("Bulan (dalam Hari) : ", P.getBulan())
    print("Laba Harian : ", L)
    print("Laba Bulanan : ", K)    
