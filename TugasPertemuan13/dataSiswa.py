daftar_siswa = []

while True :
    print("\n==== APLIKASI DAFTAR NILAI SEDERHANA ====")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan seluruh data")
    print("3. Tampilkan statistik Nilai")
    print("4. Cari data siswa berdasarkan nama")
    print("5. Keluar Program")

    pilihan = input("Pilih menu (1 - 5) : ")

    if pilihan == "1" :
        nama = input ("Masukan nama siswa : " ).strip()
        nilai = float(input("Masukan nilai siswa : "))
        daftar_siswa.append ([nama, nilai])
        print("Data Berhasil ditambahkan")

    elif pilihan == "2" :
        if len(daftar_siswa) == 0 :
            print("Belum ada data siswa.")
        else :
            print("\nDAFTAR NILAI SISWA")
            for i , siswa in enumerate(daftar_siswa) :
                print(f"{i + 1}. {siswa[0]} - {siswa[1]}")

    elif pilihan == "3" :
        if len(daftar_siswa) == 0 :
            print("Belum ada data untuk dihitung.")
        else : 
            nilai_semua = [s[1] for s in daftar_siswa]
            rata = sum(nilai_semua) / len(nilai_semua)
            maksimum = max(nilai_semua)
            minimum = min(nilai_semua)

            print("STATISTIK NILAI")
            print("Rata Rata : ", rata)
            print("Nilai Tertinggi : ", maksimum)
            print("Nilai Terendah : ", minimum)

    elif pilihan == 4 : 
        cari = input("Masukan nama yang dicari : ").strip().lower()
        ditemukan = False

        for siswa in daftar_siswa :
            if siswa[0].lower() == cari :
                print("Data ditemukan :", siswa[0], "-", siswa[1])
                ditemukan = True

        if not ditemukan :
            print("Data siswa tidak ditemukan!")

    elif pilihan == 5 : 
        print("Terimakasih, Program Selesai")
        break
    else : 
        print("Pilihan tidak valid , Silahkan ulangi.")

    ulang = input("\nIngin kembali ke menu utama? (y/t : )").lower()
    if ulang != "y" :
        print("Program berakhir. Terimakasih.")
        break