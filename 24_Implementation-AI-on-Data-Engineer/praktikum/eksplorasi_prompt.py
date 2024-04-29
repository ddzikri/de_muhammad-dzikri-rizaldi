import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

# Memuat kredensial API dari file .env
load_dotenv()
my_api = os.getenv("NAGA_AI_KEY")

# Inisialisasi klien OpenAI
client = OpenAI(
    api_key=my_api,
    base_url='https://api.naga.ac/v1'
)

# Fungsi untuk menghasilkan respons dari AI
def generate(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

# Membaca data penjualan dari file CSV
def read_sales_data(file_path):
    return pd.read_csv(file_path)

# Path file CSV penjualan
file_path = "zara.csv"

# Membaca data penjualan dari file CSV
sales_data = read_sales_data(file_path)

# Mendapatkan daftar kolom dari dataframe
daftar_kolom = sales_data.columns.tolist()

# Membuat prompt yang terhubung dengan data penjualan
prompt = f"""Saya memiliki dataset dengan kolom {str(daftar_kolom)}, Lalu analisis dataset tersebut dan berikan rekomendasi yang dapat membantu 
            dalam pengambilan keputusan bisnis. """
    
# Memanggil fungsi generate untuk menganalisis data dan memberikan rekomendasi
analisis_zara = generate(prompt)

# Menyimpan rekomendasi ke dalam file
with open("analisis_zara.txt", "w") as f:
    f.write(analisis_zara)

# Mencetak hasil respons
print("Rekomendasi berhasil dibuat dan disimpan dalam analisis_zara.txt")
