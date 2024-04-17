# Definisi class induk
class Person:
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan):
        self.nama = nama
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.pekerjaan = pekerjaan
    
    def info(self):
        print("="*40)
        print("Nama:", self.nama)
        print("Usia:", self.usia)
        print("Jenis Kelamin:", self.jenis_kelamin)
        print("Pekerjaan :", self.pekerjaan)

# Definisi class turunan
class Dosen(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, dosen):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.dosen = dosen
    
    def info(self):
        super().info()
        print("dosen:", self.dosen)
        print("="*40)

class Mahasiswa(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, prodi):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.prodi = prodi
    
    def info(self):
        super().info()
        print("Prodi :", self.prodi)
        print("="*40)

class Staff(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, bidang):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.bidang = bidang
    
    def info(self):
        super().info()
        print("bidang:", self.bidang)
        print("="*40)

class Satpam(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, posisi):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.posisi = posisi
    
    def info(self):
        super().info()
        print("posisi:", self.posisi)
        print("="*40)

class OB(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, posisi):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.posisi = posisi
    
    def info(self):
        super().info()
        print("posisi:", self.posisi)
        print("="*40)

# Contoh penggunaan
dosen1 = Dosen("Prof. dr. H. Muhammad Ilham Ramdhani M.T.", 28, "Laki-laki", "Dosen", "Dosen Teknik")
dosen1.info()

mahasiswa1 = Mahasiswa("Kalwani", 25, "Laki-laki", "Mahasiswa", "Teknik Informatika")
mahasiswa1.info()

staff1 = Staff("Raihan", 23, "Laki-laki", "Staff", "Staff Akademik")
staff1.info()

satpam1 = Satpam("Raka", 23, "Laki-laki", "Satpam", "Satpam Gedung Mahdor")
satpam1.info()

ob1 = OB("Tono", 23, "Laki-laki", "OB", "OB Gedung Juanda")
ob1.info()

