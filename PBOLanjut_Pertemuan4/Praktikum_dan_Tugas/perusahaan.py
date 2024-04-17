# Definisi class induk
class Person:
    def __init__(self, nama, jenis_kelamin, pekerjaan):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.pekerjaan = pekerjaan
    
    def info(self):
        print("="*40)
        print("Nama:", self.nama)
        print("Jenis Kelamin:", self.jenis_kelamin)
        print("Pekerjaan :", self.pekerjaan)

# Definisi class turunan
class Manager(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, posisi, perusahaan):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.posisi = posisi
        self.perusahaan = perusahaan
    
    def info(self):
        super().info()
        print("Posisi:", self.posisi)
        print("Perusahaan :", self.perusahaan)
        print("="*40)

class Programer(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, progammer, gaji):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.progammer = progammer
        self.gaji = gaji
    
    def info(self):
        super().info()
        print("Bidang Pekerjaan:", self.progammer)
        print("Gaji :", self.gaji)
        print("="*40)

class Teknisi(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, bidang_pekerjaan, keahlian):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.bidang_pekerjaan = bidang_pekerjaan
        self.keahlian = keahlian
    
    def info(self):
        super().info()
        print("Bidang Pekerjaan:", self.bidang_pekerjaan)
        print("Keahlian :", self.keahlian)
        print("="*40)

class Staff(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, jabatan, skill):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.jabatan = jabatan
        self.skill = skill
    
    def info(self):
        super().info()
        print("Bidang Pekerjaan:", self.jabatan)
        print("Soft Skill :", self.skill)
        print("="*40)

# Contoh penggunaan
manager1 = Manager("Muhammad Ilham Ramdhani", "Laki-laki", "Manager", "Manager", "PT. Mencari CInta Sejati")
manager1.info()

programer1 = Programer("Kalwani", "Laki-laki", "Progammer", "Front-End Development", "Rp. 271 Triliun")
programer1.info()

teknisi1 = Teknisi("Raihan", "Laki-laki", "Teknisi", "Teknisi Kabel Fiber Optic", "Komunikasi Data dan Jaringan")
teknisi1.info()

staff1 = Staff("Rama", "Laki-laki", "Staff", "Staff IT", "Problem Solving & skill issue")
staff1.info()