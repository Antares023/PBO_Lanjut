try:
    pilihan = int(input('Masukkan angka lebih dari 0 :'))
    assert pilihan > 0 # cek nilai
except AssertionError :
    print("Angka tidak boleh Nol atau negatif")