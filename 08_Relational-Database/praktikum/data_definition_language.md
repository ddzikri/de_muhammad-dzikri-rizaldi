## DATA DEFINITION LANGUAGE

1. Create database alta_online_shop.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-1.png?raw=true)

2. Dari schema Olshop yang telah kamu kerjakan di, Implementasikanlah menjadi table pada MySQL. (Seperti Sebelumnya)
    a. Create table user.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-2-A.png?raw=true)

    b. Create table product, product type, operators, product description, payment_method.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-2-B.png?raw=true)

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-2-B(2).png?raw=true)

    c. Create table transaction, transaction detail.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-2-C.png?raw=true)

3. Create tabel kurir dengan field id, name, created_at, updated_at.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-3.png?raw=true)

4. Tambahkan ongkos_dasar column di tabel kurir.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-4.png?raw=true)

5. Rename tabel kurir menjadi shipping.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-5.png?raw=true)

6. Hapus / Drop tabel shipping karena ternyata tidak dibutuhkan.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-6.png?raw=true)

7. Silahkan menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many. Seperti:
    a. 1-to-1: payment method description.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-7-A.png?raw=true)

    b. 1-to-many: user dengan alamat.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-7-B.png?raw=true)

    c. many-to-many: user dengan payment method menjadi user_payment_method_detail.

    ![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/08_Relational-Database/screenshot/DDL_NO-7-C.png?raw=true)
