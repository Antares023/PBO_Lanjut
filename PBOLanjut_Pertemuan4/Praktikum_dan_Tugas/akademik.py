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
class Dosen(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, email, induk, dosen):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.Email = email
        self.NIDN = induk
        self.dosen = dosen
    
    def info(self):
        super().info()
        print("Email :", self.Email)
        print("NIDN :", self.NIDN)
        print("dosen:", self.dosen)
        print("="*40)

class Mahasiswa(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, kelas, NIM, prodi):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.Kelas = kelas
        self.NIM = NIM
        self.prodi = prodi
    
    def info(self):
        super().info()
        print("Kelas :", self.Kelas)
        print("NIM :", self.NIM)
        print("Prodi :", self.prodi)
        print("="*40)

class Staff(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, NIP, bidang):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.NIP = NIP
        self.bidang = bidang
    
    def info(self):
        super().info()
        print("NIP :", self.NIP)
        print("bidang :", self.bidang)
        print("="*40)

class Satpam(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, KTP, gaji, posisi):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.KTP = KTP
        self.Gaji = gaji
        self.posisi = posisi
    
    def info(self):
        super().info()
        print("NIK :", self.KTP)
        print("gaji :", self.Gaji)
        print("posisi :", self.posisi)
        print("="*40)

class OB(Person):
    def __init__(self, nama, jenis_kelamin, pekerjaan, KTP, posisi):
        super().__init__(nama, jenis_kelamin, pekerjaan)
        self.KTP = KTP
        self.posisi = posisi
    
    def info(self):
        super().info()
        print("NIK :", self.KTP)
        print("posisi:", self.posisi)
        print("="*40)

# Contoh penggunaan
dosen1 = Dosen("Prof. dr. H. Muhammad Ilham Ramdhani M.T.", "Laki-laki", "Dosen", "ilhamrmdhnii02@gmail.com", 220511113, "Dosen Teknik")
dosen1.info()

mahasiswa1 = Mahasiswa("Kalwani", "Laki-laki", "Mahasiswa", "TI22C", 220511113, "Teknik Informatika")
mahasiswa1.info()

staff1 = Staff("Raihan", "Laki-laki", "Staff", "2205xxxxx", "Staff Akademik")
staff1.info()

satpam1 = Satpam("Raka", "Laki-laki", "Satpam", "320917xxxxxxxxxxx", "Rp. 2.500.000,-", "Satpam Gedung Mahdor")
satpam1.info()

ob1 = OB("Tono", "Laki-laki", "OB", "320917xxxxxxxxxxx", "OB Gedung Juanda")
ob1.info()

