tahun = int(input("Masukan Tahun : "))

if tahun % 4 == 0 :
    if tahun % 100 :
        if tahun % 400 :
            print("Tahun Kabisat")
        else :
            print("Bukan Tahun Kabisat")
    else :
        print("Tahun Kabisat")
else :
    print("Bukan tahun kabisat")