while True:
    try:
        angka = float(input("Masukkan angka yang ingin dipangkatkan : "))
        pangkat = float(input("Masukkan pangkat : "))
        kuadrat = angka ** pangkat
        assert angka > 0
        # Untuk pangkat diperbolehkan negatif
        break # Keluar dari loop jika input valid
    except AssertionError :
        print("Angka tidak boleh Nol atau negatif")
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", kuadrat)