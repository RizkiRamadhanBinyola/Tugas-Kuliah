namaKaryawan = input("Masukan Nama Karyawan : ")
gajiPokok = int(input("Masukan gaji pokok : "))
Tunjangan = int(input("Masukan Jumlah Tunjangan : "))


gajiKotor = gajiPokok + Tunjangan
potonganPajak = 0.1
gajiBersih = gajiKotor - potonganPajak

print(gajiBersih)