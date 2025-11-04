beratBadan = float(input("Masukan berat badan anda (kg): "))
tinggiBadan = float(input("Masukan tinggi badan anda (cm): "))

IMT = beratBadan / ((tinggiBadan / 100) ** 2)

print(f"IMT Anda adalah: {IMT:.2f}")

if IMT < 18.5 :
    print ("Berat Badan dikategori Kurang sehat")
elif 18.5 <= IMT <= 24.9  :
    print ("Berat Badan dikategori Normal/Sehat")
elif 25 <= IMT <= 29.9 :
    print("Berat Badan dikategori Berlebih")
else :
    print("Berat Badan dikategori Obesitas")