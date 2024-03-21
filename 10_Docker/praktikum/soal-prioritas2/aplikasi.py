import numpy as np

def calculate_average(numbers):
    average = np.mean(numbers)
    return average

if __name__ == "__main__":
    numbers = np.array([1, 2, 3, 4, 5])
    # Panggil fungsi untuk menghitung rata-rata
    result = calculate_average(numbers)
    print("Rata-rata:", result)
