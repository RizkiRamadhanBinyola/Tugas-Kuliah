import random
import os
import datetime

print("="*40)
print("    PROGRAM MENGHITUNG ANGKA ACAK   ")
waktuMulai = datetime.datetime.now()
print("Program dimulai : ", waktuMulai)
print("="*40)

angkaAcak = random.randint(1, 100)
print("Hasil angka :", angkaAcak)

menyimpanFile = input("Apakah anda ingin menyimpan hasil? (y/n) : ")

if menyimpanFile == 'y' :
    menyimpanFile == True
    namaFile = input("Masukan Nama File dan Format File : ").strip()
    if not namaFile.lower().endswith(".txt"):
        namaFile += ".txt"
    path = os.path.join(os.getcwd(), namaFile)
    with open(path, "w") as file:
        file.write(f"Hasil Angka : {angkaAcak}\n")
        print(f"File {namaFile} berhasil dibuat pada dir : {os.getcwd()}")
elif menyimpanFile == 't' :
    menyimpanFile == False

waktuSelesai = datetime.datetime.now()
waktuEksekusi = waktuSelesai - waktuMulai

print("="*40)
print("Program selesai pada:", waktuSelesai.strftime("%d-%m-%Y %H:%M:%S"))
print("Waktu eksekusi program:", waktuEksekusi.total_seconds(), "detik")
print("="*40)

