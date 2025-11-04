hargaBarang = float(input("Masukan harga barang : "))
jumlahBarang = int(input("Masukan jumlah yang di beli : "))

totalHarga = hargaBarang * jumlahBarang

if totalHarga > 500000 :
    diskon = totalHarga * 0.10
    totalBayar = totalHarga - diskon
    print(int(totalBayar))
else :
    print(totalHarga)