class Biodata :
    def __init__(self, nama, umur, status):
        self.nama=nama
        self.umur=umur
        self.status=status

    def info(self):
        print(f"Nama : {self.nama}\nUmur : {self.umur}\nStatus : {self.status}")

bio=Biodata("Ilham", "20", "Mahasiswa")
bio.info()