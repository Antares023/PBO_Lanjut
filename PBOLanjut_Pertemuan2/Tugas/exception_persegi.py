while True:
    try:
        sisi = float(input("Masukkan angka ke sisi :"))
        luas = sisi * 2
        assert sisi > 0
        break # Keluar dari loop jika input valid
    except AssertionError:
        print("Angka tidak boleh Nol atau Negatif!")
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", luas)