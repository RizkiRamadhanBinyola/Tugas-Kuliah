def for1sampai100() :
    for i in range(1,101,1) :
        print(i, end=' ')

def forcountsum() :
    awal = int(input("Masukan bilangan awal : "))
    akhir = int(input("Masukan bilangan akhir : "))

    count = 0 
    sum = 0

    print(f"Bilangan antara {awal} & {akhir}")
    for i in range(awal,akhir+1) :
        print(i, end=' ')
        count = count + 1
        sum = sum + i

        print("Bilangan di atas ada bilangan : ", count)
        print("Jumlah Semua bilangan adalah :", sum)

def latihanFor() :
    start = 1
    end = 101

    hasil_kali = 1  # mulai dari 1 karena kita menghitung PERKALIAN

    for i in range(start, end, 3):
        print(i, end=' ')
        hasil_kali *= i   # perkalian

    print("\nHasil perkalian semua bilangan =", hasil_kali)


def forList() :
    listKota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar'] 
    for kota in listKota : 
        print(kota)

def forRange() :
    for i in range(5): 
        print("Perulangan ke -", i)
def forTuple() :
    tupleBuah = ('Mangga', 'Jeruk', 'Apel', 'Pepaya') 
    for buah in tupleBuah: 
        print(buah)


def forString() :
    for karakter in "Indonesia🇮🇩": 
        print(karakter)

def forBreakContinue() :
    for i in range(10, 20): 
    # skip jika i == 15 
        if (i == 15): 
            continue
        print(i)

def forElse() :
    listKota = [ 'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar'] 
    for kota in listKota : 
        print(kota) 
    else: 
        print('Tidak ada lagi item yang tersisa')

def forElseBreak() :
    print("Jika kita gabungkan for,else dengan break, maka blok else hanya akan dieksekusi jika perintah break tidak dieksekusi.")
    listKota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar' ] 

    kotaYangDicari = input('Ketik nama kota yang kamu cari: ')
 
    for i, kota in enumerate(listKota): 

        # kita ubah katanya ke lowercase agar # menjadi case insensitive 
        if kota.lower() == kotaYangDicari.lower(): 
            print('Kota yang anda cari berada pada indeks', i) 
            break 
        else: 
            print('Maaf, kota yang anda cari tidak ada')

def forBertingkat():
    banyakMhs = int(input('Banyak Mahasiswa : '))
    for M in range(banyakMhs):
        print('Mahasiswa ke-', M+1)
        banyakMK = int(input('Banyak Matakuliah yang diambil: '))
        
        totalnilai = 0
        for N in range(banyakMK):
            nilai = int(input(f"Input nilai ke-{N+1} : "))
            totalnilai += nilai
        
        rerata = totalnilai / banyakMK
        print('Rata-Rata: ', rerata)


def forTunggal() :
    for i in [12,16,17,24,29] :
        if i % 2 == 1 :
            break
        print(i)
    print("Selesai")

def forPemilihanIf() :
    nilaiawal = int(input("Masukan Nilai awal :"))
    nilaiakhir = int(input("Masukan nilai akhir : "))

    for i in range(nilaiawal,nilaiakhir+1) :
        if i % 2 == 0 :
            print(i, " adalah bilangan Genap ")
        else :
            print(i," adalah bilangan Ganjil ")

def forIfElseBertingkat() :
    banyakBil = int(input("Masukan Banyak bilangan : "))

    for i in range (banyakBil+1) :
        bil = int(input("Masukan Bilangan : "))
        if bil > 0 :
            print(bil, " adalah bilangan positif")
        elif bil == 0 :
            print(bil, " adalah bilangan nol")
        else :
            print(bil," adalah bilangan negatif")

def forPemilihanIFELSE() :
    bil = int(input("Masukan Bilangan : "))
    for i in range (1, bil+1) :
        for j in range(1,bil+1) :
            if i == j :
                print(i , end=' ')
            else :
                print(end=' ')
            print()

def perulanganWhile() :
    jawab = 'ya'
    hitung = 0

    while(jawab == 'ya') :
        hitung += 1
        jawab = input("Ulang atau Tidak? ")
    print(f"Total perulangan : {hitung}")

while True:
    print("==== MENU UTAMA =====")
    print("1. For 1 Sampai 100")
    print("2. For Count & Sum")
    print("3. Latihan For & Hasil Perkalian pencacahan 3")
    print("4. For pada List")
    print("5. For pada Range")
    print("6. For pada Tuple")
    print("7. For pada String")
    print("8. For Break & Continue")
    print("9. For Menggunakan Else")
    print("10. For Else + Break")
    print("11. For Bertingkat")
    print("12. penggunaan for dengan bentuk pemilihan tunggal")
    print("13. For dengan bentuk pemilihan if else")
    print("14. for dengan bentuk pemilihan if else bertingkat")
    print("15. Perulangan While")
    print("16. Selesai")
    pilihan = input("Pilih menu (1-16): ")
    if pilihan == "1":
        for1sampai100()
    elif pilihan == "2":
        forcountsum()
    elif pilihan == "3":
        latihanFor()
    elif pilihan == "4":
        forList()
    elif pilihan == "5":
        forRange()
    elif pilihan == "6" :
        forTuple()
    elif pilihan == "7":
        forString()
    elif pilihan == "8":
        forBreakContinue()
    elif pilihan == "9":
        forElse()
    elif pilihan == "10":
        forElseBreak()
    elif pilihan == "11":
        forBertingkat()
    elif pilihan == "12":
        forTunggal()
    elif pilihan == "13":
        forIfElseBertingkat()
    elif pilihan == "14":
        forPemilihanIFELSE()
    elif pilihan == "15":
        perulanganWhile()
    elif pilihan == "16":
        print("Program selesai.")
        break;
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

        