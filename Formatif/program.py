def konversiSuhu():
    print("=== Konversi Suhu ===")
    pilihan = input("Ketik 'C' jika dari Celsius ke Fahrenheit, atau 'F' jika sebaliknya: ").upper()
    suhu = float(input("Masukkan suhu: "))

    if pilihan == "C":
        hasil = (suhu * 9/5) + 32
        print(f"Hasil: {hasil} °F")
    elif pilihan == "F":
        hasil = (suhu - 32) * 5/9
        print(f"Hasil: {hasil} °C")
    else:
        print("Pilihan tidak valid!")

def ganjilGenap():
    print("=== Cek Ganjil / Genap ===")
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print("Angka tersebut adalah GENAP")
    else:
        print("Angka tersebut adalah GANJIL")

def hitungLuas():
    print("=== Hitung Luas Segitiga ===")
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah {luas}")

while True:
    print("==== MENU UTAMA =====")
    print("1. Konversi Suhu (Celsius ↔ Fahrenheit)")
    print("2. Cek Ganjil / Genap")
    print("3. Hitung Luas Segitiga")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    if pilihan == "1":
        konversiSuhu()
    elif pilihan == "2":
        ganjilGenap()
    elif pilihan == "3":
        hitungLuas()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
