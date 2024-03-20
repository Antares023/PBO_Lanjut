class Kontak :
    def __init__(self, nama, kontak):
        self.nama=nama
        self.kontak=kontak

    def info(self):
        print(f"Nama : {self.nama}\nKontak : {self.kontak}")

cp=Kontak("Ilham", "+62812 xxxx xxxx")
cp.info()