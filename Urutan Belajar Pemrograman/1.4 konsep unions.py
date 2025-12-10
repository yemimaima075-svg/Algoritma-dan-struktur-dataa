# union_sederhana.py

class Union:
    def __init__(self):
        self.data = None  # 1 variabel untuk semua tipe

# Membuat objek union
u = Union()

# Menyimpan integer
u.data = 123
print("Sebagai integer :", u.data)

# Menyimpan float
u.data = 45.6
print("Sebagai float   :", u.data)

# Menyimpan string
u.data = "Hello"
print("Sebagai string  :", u.data)

#hasil modifikasi
# union_sederhana_modifikasi.py

class Union:
    def __init__(self):
        self.data = None  # satu variabel untuk semua tipe

# Membuat objek union
u = Union()

print("=== Simulasi Union Sederhana ===")

# Menyimpan integer
u.data = 100
print("1. Disimpan sebagai integer :", u.data)

# Menyimpan float
u.data = 12.75
print("2. Disimpan sebagai float   :", u.data)

# Menyimpan string
u.data = "Belajar Union"
print("3. Disimpan sebagai string  :", u.data)

# Menyimpan boolean
u.data = True
print("4. Disimpan sebagai boolean :", u.data)

# Menyimpan list
u.data = [1, 2, 3]
print("5. Disimpan sebagai list    :", u.data)

# Menampilkan tipe data terakhir
print("\nTipe data terakhir yang tersimpan:", type(u.data).__name__)
