Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/soal_eksplorasi.png)

Kriteria yang harus dipenuhi:

a. Task pertama bertujuan untuk membuat tabel dengan nama fruits untuk menyimpan data buah-buahan.
b. Task kedua bertujuan untuk mendapatkan data dari API. Endpoint API yang digunakan adalah sebagai berikut: https://www.fruityvice.com/api/fruit/family/Rosaceae 
c. Task ketiga bertujuan untuk memasukkan data buah-buahan ke dalam tabel fruits yang sudah dibuat. 
d. Gunakan Operator berdasarkan jenis task yang dijalankan.

jawaban

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/graph_eksplorasi.png)