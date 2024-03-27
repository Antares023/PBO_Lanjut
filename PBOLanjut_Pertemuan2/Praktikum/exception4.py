try:
    f = open("file.txt", "r")
    # Proses membaca file
except FileNotFoundError:
    print("File Tidak Ditemukan")