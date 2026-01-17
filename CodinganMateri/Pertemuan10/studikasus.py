while True :
    print("="*40)
    namaPenumpang = str(input("Masukan nama anda : "))
    kodeBus = str(input("Masukan Kode Bus [R/S/H] : ")).upper()
    jumlahBeli = int(input("Masukan jumlah beli : "))

    if kodeBus == "R" :
        namaBus = "Rosalia"
        tujuanBus = str(input("Masukan Tujuan Bus R = SBY,MLG  ")).upper()
        if tujuanBus == "SBY" :
            harga = 300000
            totalHarga = harga * jumlahBeli
        elif tujuanBus == "MLG" :
            harga = 400000
            totalHarga = harga * jumlahBeli
        else :
            print("Tujuan tidak sesuai!")
            ulangProgram = str(input("Ingin Memulai ulang?(Y/N) : ").upper())
            if ulangProgram == "Y" :
                continue
            else :
                print("Program di hentikan.")
                break

    elif kodeBus == "S" :
        namaBus = "Sinar Jaya"
        tujuanBus = str(input("Masukan Tujuan Bus S = SLO,TGL : ")).upper()
        if tujuanBus == "SLO" :
            harga = 200000
            totalHarga = harga * jumlahBeli
        elif tujuanBus == "TGL" :
            harga = 250000
            totalHarga = harga * jumlahBeli
        else :
            print("Tujuan tidak sesuai!")
            ulangProgram = str(input("Ingin Memulai ulang?(Y/N) : ").upper())
            if ulangProgram == "Y" :
                continue
            else :
                print("Program di hentikan.")
                break

    elif kodeBus == "H"  :
        namaBus = "Hiba Utama"
        tujuanBus = str(input("Masukan Tujuan Bus H = LMP,JGY : ")).upper()
        if tujuanBus == "LMP" :
            harga = 200000
            totalHarga = harga * jumlahBeli
        elif tujuanBus == "JGY" :
            harga = 250000
            totalHarga = harga * jumlahBeli
        else :
            print("Tujuan tidak sesuai!")
            ulangProgram = str(input("Ingin Memulai ulang?(Y/N) : ").upper())
            if ulangProgram == "Y" :
                continue
            else :
                print("Program di hentikan.")
                break  
    else :
        print("Tujuan tidak sesuai!")
        ulangProgram = str(input("Ingin Memulai ulang?(Y/N) : ").upper())
        if ulangProgram == "Y" :
            continue
        else :
            print("Program di hentikan.")
            break  

    print("="*40)
    print("Nama Penumpang : ",namaPenumpang)
    print("Nama Bus : ",namaBus)
    print("Tujuan : ",tujuanBus)
    print("Harga Tiket : ",harga)
    print("Jumlah Beli : ",jumlahBeli)
    print("Total Harga : ",totalHarga)
    print("="*40)
    break