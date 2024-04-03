class Persegipanjang:
    def __init__(self, panjang, lebar):
        self.__panjang = 0
        self.__lebar = 0
        self.__setPanjang(panjang)
        self.__setLebar(lebar)
        
    def getPanjang(self):
        return self.__panjang
    
    def getLebar(self):
        return self.__lebar
    
    def __setPanjang(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__panjang = nilai
    
    def __setLebar(self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__lebar = nilai
        
    def Luas(self):
        L = self.__panjang * self.__lebar
        return L
    
    def keliling(self):
        K = (2* self.__panjang) + (2* self.__lebar)
        return K
    
try:
    panjang = int(input("Masukkan nilai panjang : "))
    lebar = int(input("Masukkan nilai lebar : "))
except ValueError:
    print("Masukkan hanya angka saja!")
else :
    P = Persegipanjang(panjang, lebar)
    L = P.Luas()
    K = P.keliling()
    print("Panjang : ", P.getPanjang())
    print("Lebar : ", P.getLebar())
    print("Luas Persegi Panjang : ", L)
    print("Keliling Persegi Panjang : ", K)    
