# struktur_sederhana.py

# Membuat struktur menggunakan class
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Membuat objek dari struktur
mhs1 = Mahasiswa("Yemima", "D0425305", "Sistem informasi")

# Menampilkan data
print("Data Mahasiswa:")
print("Nama    :", mhs1.nama)
print("NIM     :", mhs1.nim)
print("Jurusan :", mhs1.jurusan)

#hasil modifikasi
# struktur_sederhana_modif.py

# Membuat struktur menggunakan class
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Method untuk menampilkan data
    def tampilkan_data(self):
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Jurusan :", self.jurusan)
        print("-------------------------")

# Membuat beberapa objek dari struktur
mhs1 = Mahasiswa("Yemima", "D0425307", "sistem informasi")
mhs2 = Mahasiswa("dewi susanti", "D0425307", "Sistem Informasi")

# Menampilkan data
print("Data Mahasiswa:")
mhs1.tampilkan_data()
mhs2.tampilkan_data()
