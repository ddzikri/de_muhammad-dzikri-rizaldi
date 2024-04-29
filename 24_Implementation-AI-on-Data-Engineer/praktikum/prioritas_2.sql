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

SELECT 
    DATE_FORMAT(tanggal_transaksi, "%Y-%m") AS bulan,
    kategori_produk,
    SUM(jumlah_penjualan) AS total_penjualan,
    SUM(harga) AS total_harga
FROM 
    penjualan
GROUP BY 
    bulan, kategori_produk;
