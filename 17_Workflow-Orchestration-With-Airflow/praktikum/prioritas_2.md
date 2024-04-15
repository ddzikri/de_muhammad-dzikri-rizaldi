Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:
        
![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/soal_prioritas_2.png)

Kriteria yang harus dipenuhi:

a. Task pertama bertujuan untuk mendapatkan data dari API. Berikut adalah endpoint API yang digunakan: https://fakestoreapi.com/products 
b. Task kedua bertujuan untuk menulis hasil dari response API ke dalam file CSV
c. Task ketiga bertujuan untuk menulis hasil dari response API ke dalam file txt.
d. Task terakhir bertujuan untuk menampilkan pesan “done!” untuk menyatakan tugas telah selesai.
e. Gunakan Operator berdasarkan jenis task yang dijalankan.

Jawab 

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/graph_prioritas_2.png) 

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_2_get_data_from_api.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas__2_get_data_from_api.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas__2_write_to_csv.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas__2_write_to_txt.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas__2_print_done.png)
