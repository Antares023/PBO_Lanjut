import math
class Lingkaran:
    def __init__(self, jari):
        self.__jari = 0
        self.__setJari(jari)
        
    def getJari(self):
        return self.__jari
    
    def getPi(self):
        C = round(math.pi, 2)
        return C
    
    def __setJari(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__jari = nilai
    
    def Luas(self):
        L = math.pi * (self.__jari**2)
        return L
    
    def keliling(self):
        K = 2 * math.pi * self.__jari
        return K
    
while True:
    try:
        jari = int(input("Masukkan nilai Jari-jari : "))
        P = Lingkaran(jari)
        L = P.Luas()
        K = P.keliling()
        assert jari>0
        break
    except ValueError:
        print("Masukkan hanya angka saja!")
    except AssertionError:
        print("Angka tidak boleh Nol atau Negatif")


print("Jari-jari : ", P.getJari())
print("Pi : ", P.getPi())
print("Luas Lingkaran : ", L)
print("Keliling Lingkaran : ", K)