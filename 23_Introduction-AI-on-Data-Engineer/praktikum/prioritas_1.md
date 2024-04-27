Dokumentasi:

- Ambil screenshot hasil eksekusi di OpenAI Playground.

- Copy-paste input dan output ke dalam file txt.

    Input 1 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/input(1)_prioritas-1.png?raw=true)

    Kamu seorang yang bekerja sebagai data engineer. Buatkan skema database tentang Aplikasi Sistem Inventaris Barang

    Output 1 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(1)_prioritas-1.png?raw=true)

    Tentu, berikut adalah skema database sederhana untuk Aplikasi Sistem Inventaris Barang:

        1. Tabel: Barang
            - id_barang (Primary Key): ID unik untuk setiap barang.
            - nama_barang: Nama barang.
            - deskripsi: Deskripsi barang.
            - jumlah: Jumlah barang yang tersedia.
            - lokasi: Lokasi penyimpanan barang.
            - tanggal_masuk: Tanggal barang masuk ke inventaris.
            - harga_satuan: Harga satuan barang.

        2. Tabel: Kategori
            - id_kategori (Primary Key): ID unik untuk setiap kategori.
            - nama_kategori: Nama kategori barang.

        3. Tabel: Supplier

            - id_supplier (Primary Key): ID unik untuk setiap supplier.
            - nama_supplier: Nama supplier.
            - alamat: Alamat supplier.
            - telepon: Nomor telepon supplier.
            - email: Alamat email supplier.

        4. Tabel: Transaksi

            - id_transaksi (Primary Key): ID unik untuk setiap transaksi.
            - id_barang (Foreign Key): Merujuk ke ID barang dalam tabel Barang.
            - id_supplier (Foreign Key): Merujuk ke ID supplier dalam tabel Supplier.
            - tanggal_transaksi: Tanggal transaksi dilakukan.
            - jumlah_beli: Jumlah barang yang dibeli.
            - total_harga: Total harga transaksi.


    Input 2 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/input(2)_prioritas-1.png?raw=true)

    Mengesankan!! Sekarang kamu di berikan tugas untuk membuat skema database tentang Aplikasi Sistem Inventaris Barang dengan query DDL.

    Output 2 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(2)_prioritas-1.png?raw=true)

    Tentu, berikut adalah query DDL (Data Definition Language) untuk membuat skema database Aplikasi Sistem Inventaris Barang:

        -- Tabel Barang
        CREATE TABLE Barang (
            id_barang INT PRIMARY KEY AUTO_INCREMENT,
            nama_barang VARCHAR(100),
            deskripsi TEXT,
            jumlah INT,
            lokasi VARCHAR(100),
            tanggal_masuk DATE,
            harga_satuan DECIMAL(10,2)
        );

        -- Tabel Kategori
        CREATE TABLE Kategori (
            id_kategori INT PRIMARY KEY AUTO_INCREMENT,
            nama_kategori VARCHAR(100)
        );

        -- Tabel Supplier
        CREATE TABLE Supplier (
            id_supplier INT PRIMARY KEY AUTO_INCREMENT,
            nama_supplier VARCHAR(100),
            alamat TEXT,
            telepon VARCHAR(20),
            email VARCHAR(100)
        );

        -- Tabel Transaksi
        CREATE TABLE Transaksi (
            id_transaksi INT PRIMARY KEY AUTO_INCREMENT,
            id_barang INT,
            id_supplier INT,
            tanggal_transaksi DATE,
            jumlah_beli INT,
            total_harga DECIMAL(10,2),
            FOREIGN KEY (id_barang) REFERENCES Barang(id_barang),
            FOREIGN KEY (id_supplier) REFERENCES Supplier(id_supplier)
        );

    Input 3 : 

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/input(3)_prioritas-1.png?raw=true)

    Keren!! Sekarang tugas kamu buatkan query select dari skema database tersebut!

    Output 3 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(3)_prioritas-1.png?raw=true)

    Tentu, berikut adalah beberapa contoh query SELECT untuk mengekstrak informasi dari skema database Aplikasi Sistem Inventaris Barang:

        1. Mengambil semua data barang:
            SELECT * FROM Barang;
        2. Mengambil semua data kategori barang:
            SELECT * FROM Kategori;
        3. Mengambil semua data supplier:
            SELECT * FROM Supplier;
        4. Mengambil semua transaksi:
            SELECT * FROM Transaksi;
        5. Mengambil nama barang, jumlah, dan harga satuan:
            SELECT nama_barang, jumlah, harga_satuan FROM Barang;
        6. Mengambil nama supplier dan alamat:
            SELECT nama_supplier, alamat FROM Supplier;
        7. Mengambil data transaksi untuk barang tertentu:
            SELECT * FROM Transaksi WHERE id_barang = [ID_BARANG];
        8. Mengambil total harga transaksi untuk supplier tertentu:
            SELECT id_supplier, SUM(total_harga) AS total_harga FROM Transaksi WHERE id_supplier = [ID_SUPPLIER] GROUP BY id_supplier;
        9. Mengambil nama barang dan jumlah yang tersedia lebih dari 10:
            SELECT nama_barang, jumlah FROM Barang WHERE jumlah > 10;
        10. Mengambil daftar barang yang masuk pada bulan tertentu:
            SELECT * FROM Barang WHERE MONTH(tanggal_masuk) = [BULAN] AND YEAR(tanggal_masuk) = [TAHUN];

    Input 4 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/input(4)_prioritas-1.png?raw=true)

    Sangat baikk!! Lalu jelaskan tentang relational database yang terjadi  pada aplikasi Sistem Inventaris Barang!

    Output 4 : 

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(4)_prioritas-1.png?raw=true)

    Pada Aplikasi Sistem Inventaris Barang yang telah kita susun skemanya, terdapat beberapa hubungan relational antara tabel-tabel yang berbeda. Hubungan ini memungkinkan kita untuk mengaitkan data antara entitas-entitas yang berbeda dalam database. Berikut adalah hubungan relational yang terjadi:

        1. Hubungan antara Tabel Barang dan Tabel Kategori:
            - Tabel Barang memiliki kolom id_kategori yang merujuk ke kolom id_kategori dalam Tabel Kategori.
            - Ini memungkinkan kita untuk mengetahui kategori barang apa yang dimiliki oleh setiap barang dalam inventaris.
        2. Hubungan antara Tabel Barang dan Tabel Transaksi:
            - Tabel Transaksi memiliki kolom id_barang yang merujuk ke kolom id_barang dalam Tabel Barang.
            - Ini memungkinkan kita untuk mengetahui barang apa yang terlibat dalam setiap transaksi.
        3. Hubungan antara Tabel Supplier dan Tabel Transaksi:
            - Tabel Transaksi memiliki kolom id_supplier yang merujuk ke kolom id_supplier dalam Tabel Supplier.
            - Ini memungkinkan kita untuk mengetahui supplier mana yang terlibat dalam setiap transaksi.

    Melalui hubungan-hubungan ini, kita dapat melakukan query yang kompleks untuk mengekstrak informasi yang lebih terperinci, seperti melihat riwayat transaksi dari suatu supplier tertentu, mengetahui kategori barang yang paling sering dibeli, atau melihat transaksi-transaksi yang melibatkan barang dengan jumlah tertentu. Hal ini memungkinkan Aplikasi Sistem Inventaris Barang untuk mengelola data secara efisien dan memberikan informasi yang berguna kepada pengguna.

Penjelasan Hasil:

    - Buat penjelasan singkat mengenai bagaimana AI memproses input dan menghasilkan output.

    - Jelaskan potensi aplikasi hasil ini dalam konteks Data Engineering.
