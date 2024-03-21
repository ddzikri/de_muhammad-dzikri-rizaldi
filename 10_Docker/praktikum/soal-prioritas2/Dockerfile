# Gunakan base image Python
FROM python:3.9-slim

# Install package numpy
RUN pip install numpy

# Copy aplikasi Anda ke dalam container
COPY aplikasi.py /aplikasi/aplikasi.py

# Atur working directory di dalam container
WORKDIR /aplikasi
