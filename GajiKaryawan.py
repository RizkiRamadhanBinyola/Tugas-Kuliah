gajiPokok = float(input("Masukkan gaji pokok: "))
Tunjangan = float(input("Masukkan tunjangan: "))
Potongan = float(input("Masukkan potongan: "))

gajiBersih = gajiPokok + Tunjangan - Potongan

print(f"Gaji Bersih Karyawan adalah: Rp{gajiBersih:,.2f}")