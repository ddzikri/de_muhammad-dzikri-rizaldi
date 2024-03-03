class KelasLatihan:
    def __init__(self, jenis_latihan, jadwal, kapasitas):
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal
        self.kapasitas = kapasitas
        self.peserta = []

    def tampilkanInfo(self):
        print(f"Jenis Latihan   : {self.__jenis_latihan}")
        print(f"Jadwal Latihan  : {self.__jadwal}")
        print(f"Kapasitas       : {self.kapasitas}")
        print(f"Jumlah Peserta  : {len(self.peserta)}")
    
    def pesanKelas(self, nama_peserta):
        if len(self.peserta) < self.kapasitas:
            self.peserta.append(nama_peserta)
            print(f"{nama_peserta} berhasil memesan kelas {self.__jenis_latihan}")
        else:
            print("Maaf, kelas sudah penuh.")

    def batalkanKelas(self, nama_peserta):
        if nama_peserta in self.peserta:
            self.peserta.remove(nama_peserta)
            print(f"{nama_peserta} berhasil membatalkan kelas {self.__jenis_latihan}")
        else:
            print(f"{nama_peserta} tidak terdaftar dalam kelas ini.")


class Yoga(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, kapasitas, tingkat_kesulitan):
        super().__init__(jenis_latihan, jadwal, kapasitas)
        self.__tingkat_kesulitan = tingkat_kesulitan

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat Kesulitan:", self.__tingkat_kesulitan)

    def pesanKelas(self, nama_peserta):
        if len(self.peserta) < self.kapasitas:
            if "sakit" in nama_peserta.lower():
                print("Maaf, peserta yang sedang sakit tidak dapat mendaftar untuk kelas Yoga.")
            else:
                super().pesanKelas(nama_peserta)
        else:
            print("Maaf, kelas Yoga sudah penuh.")

class AngkatBeban(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, kapasitas, berat_maksimum):
        super().__init__(jenis_latihan, jadwal, kapasitas)
        self.__berat_maksimum = berat_maksimum

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Berat Maksimum yang Dapat Diangkat:", self.__berat_maksimum)

    def pesanKelas(self, nama_peserta):
        if len(self.peserta) < self.kapasitas:
            if "cedera" in nama_peserta.lower():
                print("Maaf, peserta dengan cedera tidak dapat mendaftar untuk kelas AngkatBeban.")
            else:
                super().pesanKelas(nama_peserta)
        else:
            print("Maaf, kelas AngkatBeban sudah penuh.")


kelas_yoga = Yoga("Yoga", "Senin", 10, "Sulit")
kelas_angkat_beban = AngkatBeban("Angkat Beban", "Rabu", 8, 100)

kelas_yoga.pesanKelas("John mendaftar untuk kelas Yoga")
kelas_yoga.batalkanKelas("John membatalkan pendaftaran untuk kelas Yoga")
print("\n")
kelas_angkat_beban.pesanKelas("Mike mendaftar untuk kelas Angkat Beban ")
kelas_yoga.batalkanKelas("John membatalkan pendaftaran untuk kelas Yoga")

print("\nInfo kelas setelah pemesanan:")
kelas_yoga.tampilkanInfo()
print("\n")
kelas_angkat_beban.tampilkanInfo()
