def ambil_nilai(kamus, kunci):
    try:
        nilai = kamus[kunci]
        print("Nilai dari kunci", kunci, "adalah : ", nilai)
    except KeyError:
        print("Error: Kunci", kunci, "tidak ditemukan di dalam kamus")
    
# Contoh pemanggilan fungsi dengan kunci yang tidak ada
data = {'nama': 'John', 'usia': 30, 'kota': 'Jakarta'}

kunci = input("Masukkan kunci [nama, usia, kota]:")
ambil_nilai(data, kunci)