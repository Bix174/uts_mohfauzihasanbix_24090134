berat = float(input("Masukkan Berat Badan (Kg): "))
tinggi = float(input("Masukkan Tinggi Badan (M): "))
hasil_timbang = berat // tinggi
if bmi < 18.5:
        hasil_timbang 'berat badan kurang'
    elif 18.5 <= bmi < 24.9:
        hasil_timbang "Berat badan normal"
    elif 25 <= bmi < 29.9:
        hasil_timbang "Kelebihan berat badan"
    else:
        hasil_timbang "Obesitas"

print(f"Berat Badan : {berat} Kg")
print(f"Tinggi Badan : {tinggi} :")
print(f"Nilai BMI Anda : {bmi:.2f}")
print(f"Kategori BMI : {kategori}")