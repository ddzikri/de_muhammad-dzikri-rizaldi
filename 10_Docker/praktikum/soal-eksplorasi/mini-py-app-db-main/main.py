import os
import requests
import mysql.connector

# Fungsi untuk mengirim permintaan ke API dan mengembalikan data pos
def ambil_data_pos():
    url_api = "https://jsonplaceholder.typicode.com/posts?userId=1"
    respons = requests.get(url_api)
    data = respons.json()
    return data

# Fungsi untuk memasukkan data pos ke dalam tabel MySQL
def masukkan_ke_mysql(pos):
    try:
        # Ganti parameter koneksi dengan detail database MySQL Anda
        koneksi = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USERNAME"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database=os.environ.get("MYSQL_NAME"),
        )

        kursor = koneksi.cursor()

        # Buat tabel pos jika belum ada
        kursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                post_id INT,
                judul VARCHAR(255),
                isi TEXT
            )
        """
        )

        # Masukkan data pos ke dalam tabel
        for pos in pos:
            kursor.execute(
                """
                INSERT INTO pos (user_id, post_id, judul, isi)
                VALUES (%s, %s, %s, %s)
            """,
                (pos["userId"], pos["id"], pos["title"], pos["body"]),
            )

        koneksi.commit()
        print("Data berhasil dimasukkan ke MySQL")

        kursor.close()
        koneksi.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Langkah 1: Ambil data pos dari API
    data_pos = ambil_data_pos()

    # Langkah 2: Ekstrak informasi yang relevan dan masukkan ke dalam MySQL
    if data_pos:
        masukkan_ke_mysql(data_pos)
    else:
        print("Tidak ada data pos yang diambil dari API.")