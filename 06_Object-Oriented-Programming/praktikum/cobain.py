class KelasLatihan:
    def __init__(self, jenis_latihan, jadwal):
        self.jenis_latihan = jenis_latihan
        self.jadwal = jadwal

    def tampilkan_info(self):
        print("Jenis Latihan:", self.jenis_latihan)
        print("Jadwal Latihan:", self.jadwal)


class yoga(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(jenis_latihan, jadwal)
        self.tingkat_kesulitan = tingkat_kesulitan

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tingkat Kesulitan:", self.tingkat_kesulitan)

    def atur_posisi_yoga(self, posisi):
        print("Posisi Yoga diatur menjadi:", posisi)


class AngkatBeban(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, berat_maksimum):
        super().__init__(jenis_latihan, jadwal)
        self.berat_maksimum = berat_maksimum

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Berat Maksimum yang Dapat Diangkat:", self.berat_maksimum)

    def atur_berat_beban(self, berat):
        print("Berat Beban diatur menjadi:", berat)


# Demonstrasi Polymor
latihan1 = yoga("Yoga", "Senin", "Sulit")
latihan1.atur_posisi_yoga("Kayang")
latihan1.tampilkan_info() # Menampilkan info jenis latihan dan jadwal

latihan2 = AngkatBeban("Angkat Beban", "Rabu", 100)
latihan2.atur_berat_beban(20)
latihan2.tampilkan_info() # Menampilkan info jenis latihan dan jadwal

# Demonstrasi Polymorphism Lanjutan
def gunakan_metode_khusus(latihan_objek):
    if isinstance(latihan_objek, yoga):
        latihan_objek.atur_posisi_yoga("Roll Depan")
    elif isinstance(latihan_objek, AngkatBeban):
        latihan_objek.atur_berat_beban(30)

# Penggunaan fungsi gunakan_metode_khusus dengan objek dari masing-masing kelas
gunakan_metode_khusus(latihan1)
gunakan_metode_khusus(latihan2)
