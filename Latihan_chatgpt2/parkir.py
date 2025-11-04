jamMasuk = float(input("Masukan jam masuk : "))
jamKeluar = float(input("Masukan jam keluar : "))
tarif = int(input("Masukan tarif per-jam : "))

lamaParkir =   jamKeluar - jamMasuk
biayaParkir = lamaParkir * tarif

print(f"Lama Parkir : {int(lamaParkir)} Jam")
print("Biaya Parkir : ", int(biayaParkir))