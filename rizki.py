namaPembeli = input("Masukan Nama pembeli")

hargaSrikaya = 5000
hargaJambu = 7000.0

jumlahSrikaya = int(input("Masukan jumlah Srikaya yang dibeli"))
jumlahJambu = int(input("Masukan jumlah Jambu yang dibeli"))

totalSrikaya = hargaSrikaya * jumlahSrikaya
totalJambu = hargaJambu * jumlahJambu 
totalHarga = totalSrikaya + totalJambu

if totalHarga > 30000:
  diskon = totalHarga * 0.03
  totalBayar = totalHarga - diskon
else:
  diskon = 0
  totalBayar = totalHarga

print("Nama Pembeli:", namaPembeli)
print("Total Harga Srikaya:", totalSrikaya)
print("Total Harga Jambu:", totalJambu)
print("Total Harga Keseluruhan:", totalHarga)
print("Diskon 3%:", diskon)
print("Total yang harus dibayar:", totalBayar)