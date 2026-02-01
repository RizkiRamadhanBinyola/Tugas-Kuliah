while True :
    print("="*90)
    print("KURSUS ONLINE GANEBO")
    print("="*90)

    data = []

    jumlahData = int(input("Masukan jumlah data siswa : "))

    for i in range(jumlahData) :
        print(f"Data ke-{i+1}")
        namaSiswa = str(input("Masukan nama siswa : "))
        paketKursus = input("Masukan kode paket [1/2/3] : ").lower()

        if paketKursus == "1" :
            namaPaket = "Cerdas"
            namaMateri = "Android Programming"
            Harga = 3000000
        elif paketKursus == "2" :
            namaPaket = "Ceria"
            namaMateri = "Desain Grafis"
            Harga = 2500000
        elif paketKursus == "3" :
            namaPaket = "Smile"
            namaMateri = "Multimedia"
            Harga = 2000000
        else :
            print("Kode paket tidak sesuai")
            continue
                
        data.append([namaSiswa,namaPaket,Harga,namaMateri])

    print("="*90)
    print("REKAPITULASI PENDAFTARAN KURSUS ONLINE")
    print("="*90)
    print(f"{'No':<5}{'Nama Siswa':<20}{'Nama Paket':<20}{'Harga':<20}{'Nama Materi':<20}")

    total = 0
    for no, d in enumerate(data, 1) :
        print(f"{no:<5}{d[0]:<20}{d[1]:<20}{d[2]:<20}{d[3]:<20}")
        total += d[2]

    print("="*90)
    print("Total Bayar : ", total)
    
    uangBayar = int(input("Masukan uang anda : "))
    if uangBayar < total :
        print("Uang anda kurang ")
        ulangProgram = str(input("Ingin Memulai ulang?(Y/N) : ").upper())
        if ulangProgram == "Y" :
            continue
        else :
            print("Terimakasih Telah menggunakan program kami.")
            break
    else :
        uangKembali = uangBayar - total
        print("Uang Kembali : ", uangKembali)

    ulangProgram = str(input("Ingin Memulai ulang?(Y/N) : ").upper())
    if ulangProgram == "Y" :
        continue
    else :
        print("Program di hentikan.")
        break