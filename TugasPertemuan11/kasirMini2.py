daftarBarang = [] # List Kosong untuk inputan dari namaBarang
totalBelanja = 0 # Var dengan nilai 0 dan akan bertambah seiring inputan perulangan berjalan

while True :
    namaBarang = str(input("Masukan Nama Barang : "))
    hargaBarang = int(input("Masukan Harga Barang : "))
    daftarBarang.append((namaBarang,hargaBarang)) # untuk menambahkan data baru ke dalam list
    totalBelanja += hargaBarang # Menjumlakan semua harga barang
    # Validasi melanjutkan perulangan atau tidak
    lanjut = str(input("Ingin menambahkan Barang yang lain?(y/n) : ")[:1]) 
    # Jika tidak lanjut maka hentikan program
    if lanjut == "n" :
        break
# Hitung diskon jika totalBelanja melebihi 500000 
diskon = 0
if totalBelanja >= 500000 :
    # Maka customer mendapatkan diskon 10%
    diskon = totalBelanja * 0.10

# Total bayar setelah mendapatkan diskon
totalBayar = totalBelanja - diskon


#Print struk Pembelian 
print("\n===== STRUK PEMBELIAN =====") 

for barang, harga in daftarBarang: # perulangan untuk data barang yang tersimpan di dalam list daftarBarang[]
    print(f"- {barang} : Rp {harga}") # Menampilkan nama barang dan harga barang

print("\nTotal Belanja : Rp", totalBelanja) # Menampilkan total harga barang sebelum diskon

print("Diskon        : Rp", int(diskon)) # Menampilkan jumlah diskon yang didapatkan 

print("Total Bayar   : Rp", int(totalBayar)) # Menampilkan total yang harus dibayar setelah dikurangi diskon

print("===========================")

