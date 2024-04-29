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

# Prompt untuk membuat SQL query
sql_prompt = """Buatkan SQL query untuk menghitung total penjualan per kategori produk setiap bulan, dengan mencakup informasi 
                atribut tanggal_transaksi, jumlah_penjualan, harga, kategori_produk"""

# Fungsi untuk membuat SQL query dari prompt yang diberikan
def create_sql_query(prompt):
    result = generate(prompt)
    return result

# Menghasilkan SQL query
sql_query = create_sql_query(sql_prompt)

# Menyimpan SQL query ke dalam file jika hasil tidak None
if sql_query is not None:
    with open("sql_query.txt", "w") as f:
        f.write(sql_query)
    print("SQL query berhasil dibuat dan disimpan dalam sql_query.txt")
else:
    print("Tidak ada respons yang diberikan oleh model AI.")

# Mencetak hasil respons
print("SQL query berhasil dibuat dan disimpan dalam sql_query.txt")
