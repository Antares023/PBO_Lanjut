try:
    a = [1, 2, 3]
    b = int(input("Masukkan nomor index [0,1,2] : "))
    print(a[b])
except IndexError:
    print("Indeks di luar rentang array")
except Exception as e:
    print("Terjadi kesalahan :", e)