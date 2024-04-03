import math
class Segitiga:
    def __init__(self, alas, tinggi):
        self.__alas = 0
        self.__tinggi = 0
        self.__setAlas(alas)
        self.__setTinggi(tinggi)
        
    def getAlas(self):
        return self.__alas
    
    def getTinggi(self):
        return self.__tinggi
    
    def getSisiMiring(self):
        C = round(math.sqrt((self.__alas**2)+(self.__tinggi**2)), 2)
        return C
    
    def __setAlas(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__alas = nilai
    
    def __setTinggi(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__tinggi = nilai
        
    def Luas(self):
        L = 0.5 * self.__alas * self.__tinggi
        return L
    
    def keliling(self):
        K = round(self.getSisiMiring() + self.__alas + self.__tinggi,2)
        return K
    
try:
    alas = int(input("Masukkan nilai alas : "))
    tinggi = int(input("Masukkan nilai tinggi : "))
except ValueError:
    print("Masukkan hanya angka saja!")
else :
    P = Segitiga(alas, tinggi)
    L = P.Luas()
    K = P.keliling()
    print("alas : ", P.getAlas())
    print("tinggi : ", P.getTinggi())
    print("Luas Segitiga : ", L)
    print("Keliling Segitiga : ", K)