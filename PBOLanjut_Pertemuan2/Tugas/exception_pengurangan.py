while True:
    try:
        a = float(input("Masukkan angka ke 1 :"))
        b = float(input("Masukkan angka ke 2 :"))
        c = a - b
        break # Keluar dari loop jika input valid
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", c)
    