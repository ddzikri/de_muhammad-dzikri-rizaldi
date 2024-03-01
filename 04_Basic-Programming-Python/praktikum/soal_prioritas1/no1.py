print(25 *"*")
print("Menghitung Luas Persegi")
print(25 *"*")

# Input data dari user
panjang = float(input("Masukkan Panjang dari persegi tersebut : "))
lebar = float(input("Masukkan lebar dari persegi tersebut : "))

# perhitungan rumus
luasPersegi = panjang * lebar 
print(f"luas persegi panjang adalah : {luasPersegi}")

# mencetak kata
if luasPersegi % 2 == 0:
    print ("Even Rectangle")
else:
    print ("Odd Rectangle")