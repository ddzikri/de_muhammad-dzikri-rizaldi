FROM apache/airflow:2.7.2

COPY requirements.txt /requirements.txt 

RUN pip install --user --upgrade pip

RUN pip install --nocache--dir --user -f /requirements.txt 