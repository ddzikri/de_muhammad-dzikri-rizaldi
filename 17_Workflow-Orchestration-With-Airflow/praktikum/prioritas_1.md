1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/soal_prioritas_1.png)

Catatan:

a. Satu task menggambarkan perintah bash yang harus dijalankan.
b. Gunakan BashOperator dalam membuat DAG.

jawaban

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/graph_prioritas_1_no_1.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_1_echo_hello_airflow.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_1_mkdir_about_us.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_1_mkdir_our_work.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_1_touch_about_us.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_1_touch_our_works.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_1_echo_done.png)

2. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/soal_prioritas_1_no_2.png)

Kriteria yang harus dipenuhi:

a. Task pertama adalah membuat sekumpulan bilangan acak dari 1 sampai 50 dengan jumlah bilangan adalah 25 bilangan.
b. Task kedua adalah menghitung jumlah dari semua bilangan yang didapatkan dari task pertama.
c. Task terakhir adalah menentukan apakah jumlah dari semua bilangan merupakan bilangan genap atau bukan. Jika merupakan bilangan genap tampilkan tulisan “Even Sum”. Jika tidak maka tampilkan tulisan “Odd Sum”.
d. Gunakan X-COM dalam proses pertukaran data antar task.
e. Gunakan PythonOperator dalam membuat DAG.

jawaban

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/graph_prioritas_1_no_2.png) 

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_2_generate_random_numbers.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_2_calculate_sum.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/xcom_prioritas_1_no_2_calculate_sum.png)

![alt text](https://github.com/ddzikri/de_muhammad-dzikri-rizaldi/blob/main/17_Workflow-Orchestration-With-Airflow/screenshots/logs_prioritas_1_no_2_check_even_sum.png)