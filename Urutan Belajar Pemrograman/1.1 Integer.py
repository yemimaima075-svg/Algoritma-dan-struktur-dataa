# contoh_integer_1.py

a = 10
b = 3

print("Nilai a:", a)
print("Nilai b:", b)

# operasi matematika
print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)        # hasil float
print("Modulus (sisa bagi):", a % b)
print("Pangkat:", a ** b)

#hasil modifikasi
# contoh_string_modifikasi_lanjut.py

# input dari user
s = input("Masukkan sebuah kalimat: ")
print("Asli:", s)

# hitung huruf tertentu
huruf = input("Masukkan huruf yang ingin dihitung: ")
print(f"'{huruf}' muncul sebanyak:", s.count(huruf))

# ubah semua huruf kecil jadi besar
s_upper = s.upper()
print("Semua huruf diubah menjadi kapital:", s_upper)

# ubah semua huruf menjadi kecil
s_lower = s.lower()
print("Semua huruf diubah menjadi huruf kecil:", s_lower)

# ambil karakter pertama dan terakhir
print("Karakter pertama:", s[0])
print("Karakter terakhir:", s[-1])

# membalik seluruh kalimat
print("Kalimat dibalik:", s[::-1])

# hitung jumlah vokal
vokal = "aiueoAIUEO"
jumlah_vokal = sum(1 for x in s if x in vokal)
print("Jumlah vokal dalam kalimat:", jumlah_vokal)

# hilangkan spasi
tanpa_spasi = s.replace(" ", "")
print("Kalimat tanpa spasi:", tanpa_spasi)

# cek palindrome
if s.replace(" ", "").lower() == s.replace(" ", "").lower()[::-1]:
    print("Kalimat ini merupakan PALINDROM.")
else:
    print("Kalimat ini BUKAN palindrom.")
