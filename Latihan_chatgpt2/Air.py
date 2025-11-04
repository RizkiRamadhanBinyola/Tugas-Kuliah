namaPelanggan = input("Nama Lengkap Anda : ")
jumlahPemakaian = int(input("Jumlah Pemakaian Air : "))

if jumlahPemakaian < 10 :
    tarif = 2000
    totalTagihan = jumlahPemakaian * tarif
elif 11 <= jumlahPemakaian <= 20 :
    tarif = 2500
    totalTagihan = jumlahPemakaian * tarif
elif jumlahPemakaian > 20 :
    tarif = 3000
    totalTagihan = jumlahPemakaian * tarif

print("Nama Pelanggan : ", namaPelanggan)
print("Total Tagihan : ", totalTagihan)