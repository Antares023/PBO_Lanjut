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
class Dokter(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, spesialisasi):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.spesialisasi = spesialisasi
    
    def info(self):
        super().info()
        print("Spesialisasi:", self.spesialisasi)
        print("="*40)

class Perawat(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, bidang_kerja):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.bidang_kerja = bidang_kerja
    
    def info(self):
        super().info()
        print("Bidang Kerja:", self.bidang_kerja)
        print("="*40)

class Karyawan(Person):
    def __init__(self, nama, usia, jenis_kelamin, pekerjaan, departemen):
        super().__init__(nama, usia, jenis_kelamin, pekerjaan)
        self.departemen = departemen
    
    def info(self):
        super().info()
        print("Departemen:", self.departemen)
        print("="*40)

# Contoh penggunaan
dokter1 = Dokter("Dr. Muhammad Ilham Ramdhani", 28, "Laki-laki","Dokter", "Bedah")
dokter1.info()

perawat1 = Perawat("Kalwani", 25, "Laki-laki","Perawat", "Farmasi")
perawat1.info()

karyawan1 = Karyawan("Raihan", 23, "Laki-laki","Karyawan", "HRD")
karyawan1.info()