namaPelanggan = input("Masukan Nama anda : ")

hargaMangga = 5000
hargaApel = 10000

jumlahMangga = int(input("Jumlah Buah Mangga yang dibeli : "))
jumlahApel = int(input("Jumlah buah Apel yang dibeli : "))
totalMangga = hargaMangga * jumlahMangga
totalApel = hargaApel * jumlahApel
totalHarga = totalMangga + totalApel

if totalHarga > 30000 :
    diskon = 0.05
    totalBayar = totalHarga * diskon
    print("Total diskon yang anda dapatkan : " , diskon)
    print(totalHarga)
else : 
    diskon = 0
    totalBayar = totalHarga


print("======== STRUK BELANJA ============")
print("Nama Pembeli : ", namaPelanggan)
print("Jumlah Mangga : ", )
print("Total Mangga : ", totalMangga)
print("Total Apel : " , totalApel)
print("Total Harga : " , totalHarga)
print("diskon yang didapatkan : ",  diskon)
print("Total yang harus di bayar : " , totalBayar)
print("========== TERIMAKASIH ===========")






