hargaBarang = float(input("Masukkan harga barang: "))
jumlahBarang = int(input("Masukkan jumlah barang: "))
diskon = float(input("Masukkan diskon (%): "))

total = hargaBarang * jumlahBarang
potongan = total * (diskon / 100)
bayar = total - potongan

print("\n=== HASIL PERHITUNGAN ===")
print(f"Total Harga Sebelum Diskon : Rp {total:,.2f}")
print(f"Potongan Diskon ({diskon}%) : Rp {potongan:,.2f}")
print(f"Total Bayar Setelah Diskon : Rp {bayar:,.2f}")
