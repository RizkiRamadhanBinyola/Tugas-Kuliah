# anggota_lama = ["Andi", "Budi", "Citra"]

# nama = "Dewi"
# umur = 20
# hobi = ["Membaca", "Menulis", "Coding"]

# terdaftar = nama in anggota_lama
# aktif = (umur > 18) and (len(hobi) > 1)
# data_anggota = (nama,umur,tuple(hobi),terdaftar,aktif)

# semua_hobi = set(hobi + ["Membaca", "Olahraga", "Coding"])

# print("Data Anggota : ", data_anggota)
# print("Semua Hobi anggota Klub : ", semua_hobi)

anggota_lama = ["Andi", "Budi", "Citra"]

nama = str(input("Masukan nama anda : "))
umur = int(input("Masukan umur anda : "))
hobi = input("Masukan Hobi anda ( minimal 3): ")
list_hobi = hobi.split()

if nama in anggota_lama :
    terdaftar = "Lama"
else :
    terdaftar = "Baru"

if umur > 18 and len(hobi) > 1 :
    aktif = "Aktif"
else :
    aktif = "Tidak aktif"

data_anggota = (nama,umur,hobi,terdaftar,aktif)

semua_hobi = set(list_hobi + ["Membaca", "Olahraga", "Coding"])


print("Data Anggota : ", data_anggota)
print("Semua Hobi anggota Klub : ", semua_hobi)