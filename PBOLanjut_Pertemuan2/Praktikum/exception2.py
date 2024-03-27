def hitung_akar_kuadrat(angka):
    if angka < 0:
        raise ValueError ("Angka tidak boleh negatif")
    return angka ** 0.5

try:
    input_angka = float(input("Masukkan angka non-negatif : "))
    hasil_akar = hitung_akar_kuadrat(input_angka)
    print("Akar kuadrat dari", input_angka, "adalah", hasil_akar)

except ValueError as e :
    print("Pesan kesalahan : ", e) 