# union_sederhana.py

class Union:
    def __init__(self):
        self.data = None  # satu variabel untuk semua jenis data

# Membuat objek union
u = Union()

print("=== Contoh Union Sederhana ===")

# Menyimpan integer
u.data = 10
print("Disimpan sebagai integer :", u.data)

# Menyimpan string
u.data = "Hello"
print("Disimpan sebagai string  :", u.data)

# Menyimpan float
u.data = 3.14
print("Disimpan sebagai float   :", u.data)

# Menampilkan tipe data terakhir
print("\nTipe data terakhir:", type(u.data).__name__)

#hasil modifikasi
# union_sederhana_modifikasi.py

class Union:
    def __init__(self):
        self.data = None  # satu variabel untuk semua tipe data

# Membuat objek union
u = Union()

print("=== Program Simulasi Union (Modifikasi) ===")

# Menyimpan integer
u.data = 25
print("1. Disimpan sebagai Integer :", u.data)

# Menyimpan float
u.data = 9.75
print("2. Disimpan sebagai Float   :", u.data)

# Menyimpan string
u.data = "Belajar Union"
print("3. Disimpan sebagai String  :", u.data)

# Menyimpan boolean
u.data = True
print("4. Disimpan sebagai Boolean :", u.data)

# Menyimpan list
u.data = [1, 2, 3]
print("5. Disimpan sebagai List    :", u.data)

# Menyimpan nilai dari input user
user_input = input("\nMasukkan nilai (tipe bebas): ")
u.data = user_input
print("6. Disimpan sebagai Input User:", u.data)

# Tipe data terakhir yang tersimpan
print("\nTipe data terakhir:", type(u.data).__name__)
