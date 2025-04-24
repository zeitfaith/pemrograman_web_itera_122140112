# Program Penghitung BMI
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

bmi = berat / (tinggi ** 2)

print(f"BMI Anda: {bmi:.2f}")
if bmi < 18.5:
    print("Kategori: Berat badan kurang")
elif bmi < 25:
    print("Kategori: Berat badan normal")
elif bmi < 30:
    print("Kategori: Berat badan berlebih")
else:
    print("Kategori: Obesitas")
