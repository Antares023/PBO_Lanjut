class Laba:
    def __init__(self, panjang, lebar, tinggi):
        self.__panjang = 0
        self.__lebar = 0
        self.__tinggi = 0
        self.__setPanjang(panjang)
        self.__setLebar(lebar)
        self.__setTinggi(tinggi)
        
    def getPanjang(self):
        return self.__panjang
    
    def getLebar(self):
        return self.__lebar
    
    def getTinggi(self):
        return self.__tinggi
    
    def __setPanjang(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__panjang = nilai
    
    def __setLebar(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__lebar = nilai
        
    def __setTinggi(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__tinggi = nilai
        
    def Volume(self):
        L = self.__panjang * self.__lebar * self.__tinggi
        return L
    
    def Keliling(self):
        K = 4 * (self.__panjang + self.__lebar + self.__tinggi)
        return K
    
try:
    panjang = int(input("Masukkan nilai panjang : "))
    lebar = int(input("Masukkan nilai lebar : "))
    tinggi = int(input("Masukkan nilai tinggi : "))
except ValueError:
    print("Masukkan hanya angka saja!")
else :
    P = Laba(panjang, lebar, tinggi)
    L = P.Volume()
    K = P.Keliling()
    print("Panjang: ", P.getPanjang())
    print("Lebar : ", P.getLebar())
    print("Tinggi : ", P.getTinggi())
    print("Laba Harian : ", L)
    print("Laba tinggian : ", K)    
