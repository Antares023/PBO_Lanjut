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
class Manager(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, posisi):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.posisi = posisi
    
    def info(self):
        super().info()
        print("Posisi:", self.posisi)
        print("="*40)

class Programer(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, progammer):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.progammer = progammer
    
    def info(self):
        super().info()
        print("Bidang Pekerjaan:", self.progammer)
        print("="*40)

class Teknisi(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, bidang_pekerjaan):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.bidang_pekerjaan = bidang_pekerjaan
    
    def info(self):
        super().info()
        print("Bidang Pekerjaan:", self.bidang_pekerjaan)
        print("="*40)

class Staff(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, jabatan):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.jabatan = jabatan
    
    def info(self):
        super().info()
        print("Bidang Pekerjaan:", self.jabatan)
        print("="*40)

# Contoh penggunaan
manager1 = Manager("Muhammad Ilham Ramdhani", 28, "Laki-laki", "Manager", "Manager")
manager1.info()

programer1 = Programer("Kalwani", 25, "Laki-laki", "Progammer", "Front-End Development")
programer1.info()

teknisi1 = Teknisi("Raihan", 23, "Laki-laki", "Teknisi", "Teknisi Kabel Fiber Optic")
teknisi1.info()

staff1 = Staff("Rama", 20, "Laki-laki", "Staff", "Staff IT")
staff1.info()