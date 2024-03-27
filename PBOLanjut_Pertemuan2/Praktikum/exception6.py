while True:
    try:
        input_angka = float(input("Masukkan angka :"))
        break # Keluar dari loop jika input valid
    except ValueError:
        print("Error : Masukkan harus berupa angka!")

print("Angka yang dimasukkan:", input_angka)