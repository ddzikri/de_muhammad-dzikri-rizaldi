Analisis Mendalam:

- Analisis bagaimana AI memproses input yang lebih kompleks.
        
        AI dapat menjadi alat yang berguna dalam optimasi query SQL untuk apllikasi sistem inventaris barang. Karena AI memiliki kemampuan untuk memproses input yang kompleks dan memahami konteks permintaan pengguna. Dengan input yang lebih kompleks pastinya AI akan menganalisis data yang mendalam, AI dapat mengidentifikasi area-area di mana optimasi diperlukan, seperti penggunaan indeks, optimasi query, atau perubahan skema database. Apalagi AI akan memberikan berbagai macam rekomendasi solusi karena analisis data yang mendalam tersebut.


- Identifikasi kelebihan dan keterbatasan AI dalam kasus ini.

        Kelebihan :
            - AI mampu memahami perintah dan permintaan pengguna dalam  
              bahasa alami, memungkinkan interaksi yang lebih intuitif dan mudah.

            - AI dapat melakukan analisis data yang mendalam untuk      
              mengidentifikasi pola dan masalah yang memerlukan optimasi, memungkinkan pengambilan keputusan yang lebih cerdas.
        
        Keterbatasan :
            - Meskipun AI dapat melakukan analisis data, namun 
              keterbatasan pengetahuan domain dalam aplikasi sistem inventaris barang dapat mengurangi akurasi rekomendasi solusi.
            
            -  Kemampuan AI untuk memberikan rekomendasi solusi juga
               tergantung pada kualitas dan ketersediaan data yang diberikan. Keterbatasan data dapat mengurangi akurasi rekomendasi yang diberikan oleh AI.


Dokumentasi dan Penjelasan:

- Ambil screenshot hasil eksekusi lanjutan.

- Copy-paste input dan output ke dalam file txt.
    
        Input 1 :

        Sangat baikk!! Lalu jelaskan tentang relational database yang terjadi  pada aplikasi Sistem Inventaris Barang!

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/input(1)_prioritas-2.png?raw=true)

        Output  1 :

        ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(1)_prioritas-2.png?raw=true)

        Pada Aplikasi Sistem Inventaris Barang yang telah kita susun skemanya, terdapat beberapa hubungan relational antara tabel-tabel yang berbeda. Hubungan ini memungkinkan kita untuk mengaitkan data antara entitas-entitas yang berbeda dalam database. Berikut adalah hubungan relational yang terjadi

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

        Input 2 : 

        Masuk ditahap Eksekusi Lanjutan!! Sekarang Terapkan optimasi query SQL kepada query skema database kita sebelumnya yaitu tentang Aplikasi Sistem Inventaris Barang

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/input(2)_prioritas-2.png?raw=true)

        Output 2 :

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(2)_prioritas-2.png?raw=true)

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/23_Introduction-AI-on-Data-Engineer/screenshots/output(2.1)_prioritas-2.png?raw=true)

        Tentu! Untuk menerapkan optimasi query SQL pada skema database Aplikasi Sistem Inventaris Barang, kita dapat melakukan beberapa perubahan pada query-query yang telah disediakan sebelumnya. Berikut adalah contoh-contoh perubahan yang dapat dilakukan untuk meningkatkan kinerja query:

            1. Penggunaan Indeks:
                - Tambahkan indeks pada kolom-kolom yang sering digunakan dalam kondisi WHERE, JOIN, atau ORDER BY. Misalnya, pada kolom id_barang di tabel Transaksi dan pada kolom           id_supplier di tabel Transaksi.
                    CREATE INDEX idx_id_barang ON Transaksi (id_barang);
                    CREATE INDEX idx_id_supplier ON Transaksi (id_supplier);

            2. Seleksi Kolom yang Diperlukan:
                - Pastikan hanya memilih kolom-kolom yang benar-benar diperlukan dalam hasil query. Misalnya, pada query untuk menampilkan transaksi, pilih hanya kolom-kolom yang diperlukan.
                    SELECT id_transaksi, tanggal_transaksi, jumlah_beli, total_harga FROM Transaksi;

            3. Optimasi Join:
                - Gunakan jenis join yang paling efisien untuk kasus tertentu dan pastikan tidak ada subquery yang tidak perlu.
                  Contoh:
                    SELECT Transaksi.id_transaksi, Transaksi.tanggal_transaksi, Barang.nama_barang
                    FROM Transaksi
                    INNER JOIN Barang ON Transaksi.id_barang = Barang.id_barang;
                    
            4.Penggunaan Fungsi dan Operasi:
                - Hindari penggunaan fungsi atau operasi yang mahal secara komputasi dalam kondisi WHERE atau JOIN. Pastikan operasi tersebut diperlukan dan tidak dapat dihindari.
                  Contoh:
                    SELECT * FROM Transaksi WHERE YEAR(tanggal_transaksi) = 2023;

            5. Optimasi Kondisi WHERE:
                - Perhatikan cara menulis kondisi WHERE untuk meminimalkan jumlah data yang harus diproses. Gunakan indeks jika memungkinkan.
                  Contoh:
                    SELECT * FROM Barang WHERE jumlah > 10;

            6. Menggunakan Statistik dan Profiling:
                - Gunakan alat bawaan atau eksternal untuk memonitor dan menganalisis kinerja query. Berdasarkan hasil analisis, lakukan penyesuaian yang diperlukan untuk meningkatkan   
                  kinerja.
                - Misalnya, gunakan EXPLAIN untuk menganalisis eksekusi query dan memeriksa penggunaan indeks.  

- Buat penjelasan mendalam tentang hasil dan implikasinya dalam Data Engineering.

    Dalam konteks Data engineering memiliki implikasi yang beragam seperti melakukan optimasi query, Data Engineer dapat meningkatkan kinerja sistem secara keseluruhan, memungkinkan skalabilitas yang lebih baik. Dengan mengurangi biaya operasional melalui penghematan infrastruktur dan sumber daya komputasi, perusahaan dapat meningkatkan efisiensi penggunaan sumber daya yang ada. Hal ini juga berkontribusi pada peningkatan daya saing bisnis, karena perusahaan dapat menyediakan layanan yang lebih baik dengan biaya yang lebih rendah. sehingga dapat menangani pertumbuhan data yang cepat dan meningkatkan keandalan dan ketersediaan layanan data. Oleh karena itu, hasil dari pemrosesan data yang efisien memiliki implikasi yang luas dan signifikan dalam mendukung kesuksesan bisnis perusahaan dalam era digital ini.