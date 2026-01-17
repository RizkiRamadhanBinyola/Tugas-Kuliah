# --------------------------------------
# Program Kasir Mini
# --------------------------------------

def hitung_diskon(total):
    """Menghitung diskon 10% jika total >= 500.000"""
    if total >= 500000:
        return total * 0.10
    else:
        return 0

def tampilkan_struk(daftar_barang, total, diskon, bayar):
    print("\n===== STRUK PEMBELIAN =====")
    for barang, harga in daftar_barang:
        print(f"- {barang} : Rp {harga}")
    print("-----------------------------")
    print(f"Total Belanja : Rp {total}")
    print(f"Diskon        : Rp {diskon}")
    print(f"Total Bayar   : Rp {bayar}")
    print("=============================\n")

def main():
    daftar_barang = []
    total_belanja = 0

    while True:
        nama = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))

        daftar_barang.append((nama, harga))
        total_belanja += harga

        lanjut = input("Tambah barang lain? (y/n): ").lower()
        if lanjut == "n":
            break

    diskon = hitung_diskon(total_belanja)
    total_bayar = total_belanja - diskon

    tampilkan_struk(daftar_barang, total_belanja, diskon, total_bayar)

main()
