import os
import pandas as pd
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

# Prompt untuk membuat dataset penjualan dalam format CSV
penjualan_prompt = """Buatkan dataset penjualan dengan mencakup informasi penting seperti tanggal, jumlah penjualan, harga, kategori produk, dan lainnya. 
                        Maka buatlah Dataset yang Fokus terhadap pada analisis tren penjualan, segmentasi pelanggan, dan prediksi penjualan."""

# Fungsi untuk membuat dataset dari prompt yang diberikan
def create_dataset(prompt, model="gpt-3.5-turbo"):
    result = generate(prompt, model)
    return result

# Membuat dataset penjualan dalam format CSV
penjualan_dataset = create_dataset(penjualan_prompt)

# Membuat DataFrame dari hasil respons untuk dataset penjualan
df_penjualan = pd.DataFrame({"penjualan Dataset": [penjualan_dataset]})

# Menyimpan DataFrame ke dalam file CSV
df_penjualan.to_csv("penjualan_dataset.csv", index=False)

# Mencetak hasil respons
print("Dataset penjualan berhasil dibuat dan disimpan dalam penjualan_dataset.csv")
