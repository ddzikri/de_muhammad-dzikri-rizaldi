## soal-prioritas1

1. Jelaskan perbedaan antara data terstruktur dan data tidak    terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.
    
    Jawaban
    
    Jika dilihat dari data tersetruktur yaitu diimplementasikan dalam skema yang jelas sehingga mudah untuk dianalisa maupun diintegrasikan dengan data terstruktur lainnya. Sedangkan data tidak struktur diimplementasikan dalam berbagai bentuk sehingga sangat sulit untuk dianalisa maupun diintegrasikan dengan sumber data lain. kalo berdasarkan sumber datanya data terstruktur dapat berupa transaksional, OLAP data, tradisional RDBMS, file CSV, spreadsheets. Untuk data tidak terstruktur dihasilkan oleh aplikasi-aplikasi internet, seperti data URL log, media sosial, e-mail, blog, video, dan audio.
    
    Untuk proses menyimpan data, Data terstruktur biasanya disimpan dalam relational database dengan tabel, baris serta kolom yang jelas, jadi setiap kolom mewakili variabel tertentu lalu . sedangkan Data tidak tersturktur disimpan dalam datalake yang berformat seperti file teks atau format multi media lainnya, serta memerlukan AI untuk mengolah dan memahaminya. Untuk memproses kedua jenis data tersebut, memerlukan sistem manajemen database relasional untuk data terstruktur dan data tidak struktur menggunakan teknologi machine learning yaitu hadoop atau spark.


2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.

    Jawaban
    
    jenis basis data yang menggunakan model data relasional untuk menyimpan dan mengelola informasi kedalam tabel yang saling berhubungan. Setiap tabel mewakili entitas atau objek dalam domain yang diwakili oleh basis data, dan relasi antara entitas dijelaskan sebagai melalui primary key dan foreign key. Contoh Sistem perbankan yang dimana harus mengelola akun dan transaksi pelanggan yang memungkin bank dan institusi keuangan lainnya untuk melacak dan menganalisa aktivitas user secara efektif.

3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.

    Jawaban

    Normalisasi adalah proses pembentukan struktur basis data sehingga sebagian besar ambiguity bisa dihilangkan. Normalisasi merupakan sebuah teknik dalam logical desain sebuah basis data relasional yang mengelompokkan atribut dari suatu tabel sehingga membentuk struktur tabel yang normal Adapun kriteria tabel dikatakan normal adalah ketika tidak ada kerangkapan data (redudansi data). Normalisasi penting dalam basis data relasional untuk menghilangkan nkerangkapan data sehingga meminimumkan pemakaian storage yang dipakai oleh base relations (file), Untuk mengurangi kompleksitas dan memudahkan modifikasi data.


### REFERENSI

1. Afifanto, C. (n.d.). Integrasi Data Terstruktur dan Tidak Terstruktur dalam Sistem. 
2. Puspitasri, D., Rahmad, C., & Astiningrum, M. (n.d.). Normalisasi Tabel Pada Basisdata Relasional. 
    Prosiding SENTIA 2016 – Politeknik Negeri Malang , A-341.
2. https://www.seagate.com/id/id/blog structured-vs-unstructured-data/
3. https://aws.amazon.com/id/compare/the-difference-between-structured-data-and-unstructured-data/
4. https://id.bitdegree.org/tutorial/apa-itu-basis-data-relasional/
5. https://appmaster.io/id/blog/contoh-nyata-database-relasional