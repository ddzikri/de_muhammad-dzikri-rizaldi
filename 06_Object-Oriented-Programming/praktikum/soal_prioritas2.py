from soal_prioritas1 import KelasLatihan

class yoga(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan
    
    #getter
    def get_tingkat_kesulitan (self):
        return self.__get_tingkat_kesulitan

    #setter
    def set_nama(self, tingkat_kesulitan):
        self.__tingkat_kesulitan = tingkat_kesulitan

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Tingkat Kesulitan : {self.__tingkat_kesulitan}")

yoga1 = yoga ("Kayang","Rabu","medium")
yoga1.tampilkanInfo()

class angkatBeban(KelasLatihan):
    def __init__(self,jenis_latihan, jadwal, berat_maksimum):
        super().__init__(jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum
    
    #getter
    def get_berat_maksimum (self):
        return self.__get_berat_maksimum

    #setter
    def set_nama(self, berat_maksimum):
        self.__berat_maksimum = berat_maksimum

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"berat maksimum : {self.__berat_maksimum}")

angkat_beban1 = angkatBeban ("Kayang","Rabu","medium")
yoga1.tampilkanInfo()