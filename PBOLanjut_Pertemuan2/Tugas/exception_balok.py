while True:
    try:
        panjang = float(input("Masukkan panjang :"))
        lebar = float(input("Masukkan lebar :"))
        tinggi = float(input("Masukkan tinggi :"))
        Luas_persegi_panjang = panjang * lebar * tinggi
        assert panjang > 0
        assert lebar > 0
        assert tinggi > 0
        break # Keluar dari loop jika input valid
    except AssertionError :
        print("Angka tidak boleh Nol atau negatif")
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", Luas_persegi_panjang)