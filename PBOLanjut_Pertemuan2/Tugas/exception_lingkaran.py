while True:
    try:
        a = float(input("Masukkan angka :"))
        pi = 3.14
        lingkaran = pi * (a**2)
        assert a > 0
        break # Keluar dari loop jika input valid
    except AssertionError :
        print("Angka tidak boleh Nol atau negatif")
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", lingkaran)