nilaiAngka = int(input("Masukan Nilai : "))


if nilaiAngka > 100 or nilaiAngka < 0:
    print("Nilai tidak valid, harus antara 0 - 100.")
elif 85 <= nilaiAngka <= 100:
    huruf = "A"
    print(f"Nilai Anda: {nilaiAngka} = {huruf}")
elif 70 <= nilaiAngka <= 84:
    huruf = "B"
    print(f"Nilai Anda: {nilaiAngka} = {huruf}")
elif 55 <= nilaiAngka <= 69:
    huruf = "C"
    print(f"Nilai Anda: {nilaiAngka} = {huruf}")
elif 40 <= nilaiAngka <= 54:
    huruf = "D"
    print(f"Nilai Anda: {nilaiAngka} = {huruf}")
elif 0 <= nilaiAngka < 40 :
    huruf = "E"
    print(f"Nilai Anda: {nilaiAngka} = {huruf}")
else :
    print("Nilai Tidak Valid")

# Status kelulusan
if huruf in ["A", "B", "C"]:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"Status: {status}")