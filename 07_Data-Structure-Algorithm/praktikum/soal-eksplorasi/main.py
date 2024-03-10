import uuid

class Pengeluaran:
    def __init__(self, nama, jumlah):
        self.id = str(uuid.uuid4())
        self.nama = nama
        self.jumlah = jumlah

class PengeluaranManager:
    def __init__(self):
        self.pengeluaran_list = []

    def tambah_pengeluaran(self, nama, jumlah):
        pengeluaran_baru = Pengeluaran(nama, jumlah)
        self.pengeluaran_list.append(pengeluaran_baru)
        print(f"Data added!")

    def lihat_semua_pengeluaran(self):
        if not self.pengeluaran_list:
            print("belum ada data pengeluaran.")
        else:
            print("data Pengeluaran:")
            total_pengeluaran = 0
            for pengeluaran in self.pengeluaran_list:
                print(f"ID: {pengeluaran.id}, Nama: {pengeluaran.nama}, Jumlah: {pengeluaran.jumlah}")
                total_pengeluaran += pengeluaran.jumlah
            print(f"Total Pengeluaran: {total_pengeluaran}")

    def ubah_pengeluaran(self, id_pengeluaran, nama_baru, jumlah_baru):
        for pengeluaran in self.pengeluaran_list:
            if pengeluaran.id == id_pengeluaran:
                pengeluaran.nama = nama_baru
                pengeluaran.jumlah = jumlah_baru
                print(f"data updated")
                return

    def hapus_pengeluaran(self, id_pengeluaran):
        for pengeluaran in self.pengeluaran_list:
            if pengeluaran.id == id_pengeluaran:
                self.pengeluaran_list.remove(pengeluaran)
                print(f"data deleted")
                return

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("==Menu==")
    print("1. create new expense data")
    print("2. view expense")
    print("3. update expense")
    print("4. delete expense")
    print("5. exit")

pengeluaran_manager = PengeluaranManager()

while True:
    tampilkan_menu()
    pilihan = input("enter your choice(1-5): ")

    if pilihan == "1":
        nama = input("enter exopense name: ")
        jumlah = int(input("enter amount: "))
        pengeluaran_manager.tambah_pengeluaran(nama, jumlah)
    elif pilihan == "2":
        pengeluaran_manager.lihat_semua_pengeluaran()
    elif pilihan == "3":
        id_pengeluaran = input("enter expense id: ")
        nama_baru = input("enter expense name: ")
        jumlah_baru = int(input("enter amount: "))
        pengeluaran_manager.ubah_pengeluaran(id_pengeluaran, nama_baru, jumlah_baru)
    elif pilihan == "4":
        id_pengeluaran = input("enter expense id: ")
        pengeluaran_manager.hapus_pengeluaran(id_pengeluaran)
    elif pilihan == "5":
        print("bye!")
        break
    else:
        print("invalid.")
