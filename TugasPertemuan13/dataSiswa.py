# List kosong untuk menyimpan data siswa (nama dan nilai)
daftar_siswa = []

while True:
    # Menu utama
    print("\n==== APLIKASI DAFTAR NILAI SEDERHANA ====")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan seluruh data")
    print("3. Tampilkan statistik Nilai")
    print("4. Cari data siswa berdasarkan nama")
    print("5. Keluar Program")

    # Input pilihan menu
    pilihan = input("Pilih menu (1 - 5): ")

    if pilihan == "1":
        # Input nama siswa dan hapus spasi 
        nama = input("Masukkan nama siswa: ").strip()

        # Input nilai siswa 
        nilai = float(input("Masukkan nilai siswa: "))

        # Menambahkan data ke dalam list
        daftar_siswa.append([nama, nilai])

        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        if not daftar_siswa:
            print("Belum ada data siswa.")
        else:
            print("\nDAFTAR NILAI SISWA")
            # Menampilkan data menggunakan enumerate
            for i, siswa in enumerate(daftar_siswa, start=1):
                print(f"{i}. {siswa[0]} - {siswa[1]}")


    elif pilihan == "3":
        # Cek apakah data tersedia
        if not daftar_siswa:
            print("Belum ada data untuk dihitung.")
        else:
            # Mengambil semua nilai siswa
            nilai_siswa = [siswa[1] for siswa in daftar_siswa]

            # Menghitung statistik
            rata_rata = sum(nilai_siswa) / len(nilai_siswa)
            nilai_max = max(nilai_siswa)
            nilai_min = min(nilai_siswa)

            # Menampilkan hasil statistik
            print("\nSTATISTIK NILAI")
            print("Rata-rata       :", rata_rata)
            print("Nilai tertinggi :", nilai_max)
            print("Nilai terendah  :", nilai_min)


    elif pilihan == "4":
        # Input nama yang dicari
        cari = input("Masukkan nama yang dicari: ").strip().lower()

        # Variabel penanda data ditemukan
        ditemukan = False

        # Pencarian data siswa
        for nama, nilai in daftar_siswa:
            if nama.lower() == cari:
                print(f"Data ditemukan: {nama} - {nilai}")
                ditemukan = True
                break

        # Jika data tidak ditemukan
        if not ditemukan:
            print("Data siswa tidak ditemukan!")


    elif pilihan == "5":
        print("Terima kasih, program selesai.")
        break


    else:
        print("Pilihan tidak valid, silakan ulangi.")


    ulang = input("\nKembali ke menu utama? (y/t): ").lower()
    if ulang != "y":
        print("Program berakhir. Terima kasih.")
        break
