# Input berat dan jarak 
berat = int(input("Masukkan berat paket: "))
jarak = int(input("Masukkan jarak pengiriman: "))

# Tarif berat
if berat <= 20:
    tarif_berat = 10000
elif berat <= 30:
    tarif_berat = 15000
elif berat <= 60:
    tarif_berat = 20000
else:
    tarif_berat = 45000

# Tarif jarak
if jarak <= 5:
    tarif_jarak = 2000
elif jarak <= 15:
    tarif_jarak = 5000
elif jarak <= 30:
    tarif_jarak = 10000
else:
    tarif_jarak = 15000

# Tarif total
total_tarif = tarif_berat + tarif_jarak
print(f"Tarif pengiriman: {total_tarif}" )
