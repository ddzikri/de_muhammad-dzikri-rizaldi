Sebuah perusahaan retail ingin mengoptimalkan proses analisis data penjualan mereka. Mereka memiliki dataset penjualan yang mencakup informasi seperti tanggal transaksi, jumlah penjualan, harga, kategori produk, dan lainnya. Tujuan utama adalah untuk menghasilkan SQL queries yang dapat membantu dalam analisis data yang lebih efisien dan efektif.

1. Membuat Database

    - Buatkan tabel dengan atribut kurang lebih memiliki tanggal transaksi, jumlah penjualan, harga, kategori produk, dan lainnya

        ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/24_Implementation-AI-on-Data-Engineer/screenshots/no_1_prioritas_2.png?raw=true)

        ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/24_Implementation-AI-on-Data-Engineer/screenshots/no_1.1_prioritas_2.png?raw=true)


2. Generate SQL dengan OpenAI API (Opsional):

    - Gunakan OpenAI API untuk menghasilkan SQL queries. Misalnya, berikan prompt seperti "Buatkan SQL query untuk menghitung total penjualan per kategori produk setiap bulan."

        ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/24_Implementation-AI-on-Data-Engineer/screenshots/no_2_prioritas_2.png?raw=true)

    - Catat respons AI dan analisis keakuratan serta relevansi query yang dihasilkan.

        SELECT 

            DATE_FORMAT(tanggal_transaksi, "%Y-%m") AS bulan,

            kategori_produk,

            SUM(jumlah_penjualan) AS total_penjualan,

            SUM(harga) AS total_harga

        FROM 

            penjualan

        GROUP BY 

            bulan, kategori_produk;

        Setelah dianalisis lebih lanjut Query ini cukup akurat sesuai dengan kriteria yang diberikan. Ia menghitung total penjualan untuk masing-masing kategori produk setiap bulan. Untuk mengubah tanggal transaksi menjadi format bulan-tahun yang diinginkan, ini merupakan langkah yang tepat dengan menggunakan fungsi DATE_FORMAT() dan fungsi agregasi SUM() untuk menghitung total harga dan penjualan. Lalu Query Sql ini sangat relevan dengan kriteria atribut yang dijelaskan. Ia mencakup atribut-atribut yang diminta dalam permintaan, yaitu tanggal transaksi, jumlah penjualan, harga, dan kategori produk. Selain itu, query sql juga mengelompokkan  berdasarkan bulan dan kategori produk, sesuai dengan kebutuhan untuk menghitung total penjualan per kategori produk setiap bulan.

3. Validasi Query SQL

    - Validasi SQL queries yang dihasilkan menggunakan sistem manajemen database yang ada. Pastikan query berjalan dengan benar dan menghasilkan output yang diharapkan.

        ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/24_Implementation-AI-on-Data-Engineer/screenshots/no_3_prioritas_2.png?raw=true)


4. Implementasi dan Analisis Hasil:

    - Terapkan SQL queries yang telah divalidasi dan dioptimalkan dalam sistem database perusahaan.

        Untuk menerapkan sql query dan pengotimalannya dalam sistem database perusahaan saya mungkin sudah cukup optimal, tetapi jika ingin melakukannya 
        lebih optimal lagi maka mungkin bisa diterapkan create view sebelum query menghitung total perjualan per kategori produk setiap bulan. contoh seperti dibawah 
        ini serta lampirkan juga dengan query yang telah divalidasi.

            CREATE DATABASE prioritas_2;

            USE prioritas_2;

            CREATE TABLE Penjualan (

                id INT PRIMARY KEY AUTO_INCREMENT,

                tanggal_transaksi DATE,

                jumlah_penjualan INT,

                harga DECIMAL(10, 2),

                kategori_produk VARCHAR(255),
            );

            INSERT INTO Penjualan (tanggal_transaksi, jumlah_penjualan, harga, kategori_produk)
            VALUES 
                ('2024-04-01', 10, 100.00, 'Elektronik'),

                ('2024-04-02', 15, 150.00, 'Pakaian'),

                ('2024-04-03', 8, 80.00, 'Aksesoris'),

                ('2024-04-04', 12, 120.00, 'Makanan'),

                ('2024-04-05', 20, 200.00, 'Elektronik'),

                ('2024-04-06', 18, 180.00, 'Pakaian'),

                ('2024-04-07', 25, 250.00, 'Aksesoris');

            -- Disini memang tidak akan mengubah perhitungan total perjualan tetapi secara pengoptimalan sebuah query ini merupakan paling optimal 
               tidak seperti sebelumnya.

                CREATE VIEW total_penjualan_per_bulan_per_kategori AS

                SELECT 

                    DATE_FORMAT(tanggal_transaksi, "%Y-%m") AS bulan,

                    kategori_produk,

                    SUM(jumlah_penjualan) AS total_penjualan,

                    SUM(harga) AS total_harga

                FROM 

                    penjualan

                GROUP BY 

                    bulan, kategori_produk;

                -- Query untuk menampilkan data dari view yang telah dibuat

                SELECT * FROM total_penjualan_per_bulan_per_kategori;
