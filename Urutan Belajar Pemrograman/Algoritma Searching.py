# searching_sederhana.py

angka = [10, 20, 30, 40, 50]

cari = int(input("Masukkan angka yang dicari: "))

found = False

for i in range(len(angka)):
    if angka[i] == cari:
        print(f"Angka {cari} ditemukan di index {i}")
        found = True
        break

if not found:
    print(f"Angka {cari} tidak ditemukan.")

#hasil modifikasi
# searching_sederhana_modifikasi.py

# Data array
angka = [10, 20, 30, 40, 50, 30, 20]

print("Data:", angka)

# Input angka yang dicari
cari = int(input("Masukkan angka yang dicari: "))

# Menyimpan semua index yang cocok
ditemukan = []

# Proses pencarian
for i in range(len(angka)):
    if angka[i] == cari:
        ditemukan.append(i)

# Menampilkan hasil
if len(ditemukan) > 0:
    print(f"\nAngka {cari} ditemukan sebanyak {len(ditemukan)} kali.")
    print("Pada index :", ditemukan)
else:
    print(f"\nAngka {cari} tidak ditemukan dalam array.")
