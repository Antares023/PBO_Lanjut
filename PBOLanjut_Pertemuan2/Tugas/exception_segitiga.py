while True:
    try:
        alas = float(input("Masukkan angka ke 1 :"))
        tinggi = float(input("Masukkan angka ke 2 :"))
        luas = alas * tinggi * 0.5
        assert alas > 0
        assert tinggi > 0
        break # Keluar dari loop jika input valid
    except AssertionError:
        print("Angka tidak boleh Nol atau Negatif!")
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", luas)