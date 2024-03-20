class Produk :
    def __init__(self, nama, kualitas, stok):
        self.nama=nama
        self.kualitas=kualitas
        self.stok=stok

    def info(self):
        print(f"Nama : {self.nama}\nKualitas : {self.kualitas}\nStok : {self.stok}")

gd=Produk("Hot Wheels", "Baru", "25")
gd.info()