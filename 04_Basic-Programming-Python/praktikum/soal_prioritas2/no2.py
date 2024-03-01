def skor_budget(budget):
    if budget <= 50:
        return 4
    elif budget <= 80:
        return 3
    elif budget <= 100:
        return 2
    else:
        return 1

def skor_deadline(deadline):
    if deadline <= 20:
        return 10
    elif deadline <= 30:
        return 5
    elif deadline <= 50:
        return 2
    else:
        return 1

def skor_tingkat_kesulitan(sulit):
    if sulit <= 3:
        return 10
    elif sulit <= 6:
        return 5
    elif sulit <= 10:
        return 1
    else:
        return 0

def perhitungan_skor(budget, deadline, sulit):
    hasil = skor_budget(budget) + skor_deadline(deadline) + skor_tingkat_kesulitan(sulit)
    if 17 <= hasil <= 24:
        return "High"
    elif 10 <= hasil <= 16:
        return "Medium"
    elif 3 <= hasil <= 9:
        return "Low"
    else:
        return "Impossible"

# Input
budget = int(input("Masukkan budget: "))
deadline = int(input("Masukkan Waktu Pengerjaan: "))
kesulitan = int(input("Masukkan Tingkat Kesulitan: "))

# Hitung dan Output
hasil_skor = perhitungan_skor(budget, deadline, kesulitan)
print(f"Output: {hasil_skor}")
