jumlahTiket = int(input("Masukan Jumlah Tiket : "))
statusMember = input("Mempunyai Member (y/t) : ").lower()

if statusMember == 'y' :
    statusMember == True
    total = jumlahTiket * 50000
    diskon = total * 0.20
    totalBayar = total - diskon
    print(f"Total Bayar setelah mendapatkan diskon Rp {diskon:,} : ", f"Rp {totalBayar:,}")
    print("Status anda sebagai member : ", statusMember)
elif statusMember == 't' :
    statusMember = False
    total = jumlahTiket * 50000
    totalBayar = total
    print("Total Yang Harus Anda Bayar : " , totalBayar)
    print("Status anda sebagai member : ", statusMember)