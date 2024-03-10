def prime_rectangle(height, width, start):
    nomor  = start
    jumlah_bilangan_prima = 0

    for i in range(height):
        baris = []
        for j in range(width):
            while not is_prime(nomor):
                nomor += 1
            baris.append(nomor)
            jumlah_bilangan_prima += nomor
            nomor += 1
        print(" ".join(map(str, baris)))

    # Print the sum of primes
    print(jumlah_bilangan_prima)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Contoh penggunaan
prime_rectangle(3, 2, 17)
prime_rectangle(5, 2, 1)