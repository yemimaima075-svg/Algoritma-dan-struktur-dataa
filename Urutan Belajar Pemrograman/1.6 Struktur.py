# struktur_sederhana.py

# Membuat struktur menggunakan class
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

# Membuat objek dari struktur
buku1 = Buku("Pemrograman Python", "yemima", 2025)

# Menampilkan data
print("=== Data Buku ===")
print("Judul  :", buku1.judul)
print("Penulis:", buku1.penulis)
print("Tahun  :", buku1.tahun)

#hasil modifikasi
# struktur_sederhana_modifikasi.py

# Membuat struktur menggunakan class
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

print("=== Input Data Buku ===")

# Mengambil input dari user
judul = input("Masukkan judul buku   : ")
penulis = input("Masukkan nama penulis : ")
tahun = input("Masukkan tahun terbit : ")

# Membuat objek dari struktur
buku_user = Buku(judul, penulis, tahun)

# Menampilkan data buku hasil input
print("\n=== Data Buku yang Dimasukkan ===")
print("Judul   :", buku_user.judul)
print("Penulis :", buku_user.penulis)
print("Tahun   :", buku_user.tahun)

# Tambahan: contoh buku lain (data statis)
buku2 = Buku("Belajar Algoritma", "yemima", 2025)

print("\n=== Contoh Buku Lain ===")
print("Judul   :", buku2.judul)
print("Penulis :", buku2.penulis)
print("Tahun   :", buku2.tahun)
