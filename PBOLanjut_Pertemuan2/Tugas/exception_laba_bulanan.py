while True:
    try:
        jual = float(input("Masukkan harga jual :"))
        beli = float(input("Masukkan harga beli :"))
        bulan = int(input("Masukkan total bulan dalam hari : "))
        laba = (jual - beli) * bulan
        assert jual > 0
        assert beli > 0
        assert bulan > 0
        break # Keluar dari loop jika input valid
    except AssertionError :
        print("Angka tidak boleh Nol atau negatif")
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Hasilnya adalah :", laba)
print("Dalam : ", bulan, "hari")