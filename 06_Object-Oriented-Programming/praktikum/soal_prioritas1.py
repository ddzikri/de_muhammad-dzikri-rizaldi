class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

    # Getter
    def get_nama(self):
        return self.__nama

    def get_usia(self):
        return self.__usia

    def get_id_pelanggan(self):
        return self.__id_pelanggan

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_usia(self, usia):
        self.__usia = usia

    def set_id_pelanggan(self, id_pelanggan):
        self.__id_pelanggan = id_pelanggan

    def tampilkanInfo(self):
        print(f"Nama Pelanggan: {self.__nama}")
        print(f"Usia: {self.__usia}")
        print(f"ID Pelanggan: {self.__id_pelanggan}")


class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman

    # Getter
    def get_nama(self):
        return self.__nama

    def get_spesialisasi(self):
        return self.__spesialisasi

    def get_tahun_pengalaman(self):
        return self.__tahun_pengalaman

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_spesialisasi(self, spesialisasi):
        self.__spesialisasi = spesialisasi

    def set_tahun_pengalaman(self, tahun_pengalaman):
        self.__tahun_pengalaman = tahun_pengalaman

    def tampilkanInfo(self):
        print(f"Nama Pelatih: {self.__nama}")
        print(f"Spesialisasi: {self.__spesialisasi}")
        print(f"Tahun Pengalaman: {self.__tahun_pengalaman} tahun")
        print("\n")


class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        super().__init__(nama, spesialisasi, tahun_pengalaman)
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal

    # Getter
    def get_jenis_latihan(self):
        return self.__jenis_latihan

    def get_jadwal(self):
        return self.__jadwal

    # Setter
    def set_jenis_latihan(self, jenis_latihan):
        self.__jenis_latihan = jenis_latihan

    def set_jadwal(self, jadwal):
        self.__jadwal = jadwal

    
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Jenis Latihan: {self.__jenis_latihan}")
        print(f"Jadwal Latihan: {self.__jadwal}")

pelanggan1 = Pelanggan("Dzikri", 21, "50421942")
pelanggan1.tampilkanInfo()
print("\n")

kelas_latihan1 = KelasLatihan("Jojon", "Basket", 11, "Dasar Drible", "Senin dan Kamis")
kelas_latihan1.tampilkanInfo()
