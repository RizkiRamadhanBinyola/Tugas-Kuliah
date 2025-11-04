nilaiAngka = int(input("Masukan Nilai : "))


if nilaiAngka > 100 or nilaiAngka < 0:
    print("Nilai tidak valid, harus antara 0 - 100.")
elif nilaiAngka >= 80:
    print(f"Nilai Anda: {nilaiAngka} = A")
elif nilaiAngka >= 70:
    print(f"Nilai Anda: {nilaiAngka} = B")
elif nilaiAngka >= 60:
    print(f"Nilai Anda: {nilaiAngka} = C")
elif nilaiAngka >= 50:
    print(f"Nilai Anda: {nilaiAngka} = D")
else:
    print(f"Nilai Anda: {nilaiAngka} = E")

# Status kelulusan
if nilaiAngka in ["A", "B", "C"]:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"Status: {status}")