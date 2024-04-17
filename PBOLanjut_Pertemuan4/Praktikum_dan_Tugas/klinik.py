# Definisi class induk
class Person:
    def __init__(self, nama, jenis_kelamin, pekerjaan):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.pekerjaan = pekerjaan
    
    def info(self):
        print("="*40)
        print("Nama :", self.nama)
        print("Jenis Kelamin :", self.jenis_kelamin)
        print("Pekerjaan :", self.pekerjaan)

# Definisi class turunan
class Dokter(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, nomor, spesialisasi):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.NO = nomor
        self.spesialisasi = spesialisasi
    
    def info(self):
        super().info()
        print("Nomor HP :", self.NO)
        print("Spesialisasi :", self.spesialisasi)
        print("="*40)

class Perawat(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, shift, bidang_kerja):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.shift = shift
        self.bidang_kerja = bidang_kerja
    
    def info(self):
        super().info()
        print("Shift Kerja :", self.shift)
        print("Bidang Kerja :", self.bidang_kerja)
        print("="*40)

class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, NIP, departemen):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.NIP = NIP
        self.departemen = departemen
    
    def info(self):
        super().info()
        print("NIP Karyawan :", self.NIP)
        print("Departemen:", self.departemen)
        print("="*40)

# Contoh penggunaan
dokter1 = Dokter("Dr. Muhammad Ilham Ramdhani", "Laki-laki", "Dokter", "081220489647", "Bedah")
dokter1.info()

perawat1 = Perawat("Kalwani", "Laki-laki", "Perawat", "shift pagi", "Farmasi")
perawat1.info()

karyawan1 = Karyawan("Raihan", "Laki-laki","Karyawan", "1234567890", "HRD")
karyawan1.info()