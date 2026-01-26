while True:
    dataTransaksi = []
    
    try:
        jumlahData = int(input("Masukan jumlah data siswa : "))
    except ValueError:
        print("Input harus berupa angka!")
        continue
    
    # Loop untuk mengumpulkan data
    for i in range(jumlahData):
        print(f"\nData ke-{i+1}")
        siswa = input("Masukan nama siswa : ")
        paket = input("Masukan kode paket (1/2/3) : ") # Input sebagai string agar bisa .lower() / .strip()
        
        if paket == "1":
            namaPaket, namaMateri, hargaPaket = "Cerdas", "Android Programming", 3000000
        elif paket == "2":
            namaPaket, namaMateri, hargaPaket = "Ceria", "Desain Grafis", 2500000
        elif paket == "3":
            namaPaket, namaMateri, hargaPaket = "Smile", "Multimedia", 2000000
        else:
            print("Paket Tidak Sesuai.")
            # Jika salah input, kita kurangi i agar user mengulang input data yang sama
            continue 
            
        # Gunakan kurung biasa () untuk fungsi append, dan [] untuk list di dalamnya
        dataTransaksi.append([siswa, namaPaket, hargaPaket, namaMateri])
    
    # Cetak Tabel (Di luar loop input data)
    print("\n" + "="*80)
    print(f"{'No':<5}{'Nama Siswa':<20}{'Harga':<15}{'Materi':<20}")
    print("-"*80)
    
    total = 0
    for no, d in enumerate(dataTransaksi, 1):
        print(f"{no:<5}{d[0]:<20}{d[2]:<15}{d[3]:<20}")
        total += d[2]
    
    print("="*80)
    print(f"Total Bayar: {total}")
    
    uangBayar = int(input("Masukan uang anda: "))
    if uangBayar < total:
        print("Uang anda kurang!")
    else:
        uangKembali = uangBayar - total
        print("Uang Kembali : ", uangKembali)

    ulang = input("\nIngin Memulai ulang?(Y/N) : ").upper()
    if ulang != "Y":
        print("Program dihentikan. Terima kasih!")
        break