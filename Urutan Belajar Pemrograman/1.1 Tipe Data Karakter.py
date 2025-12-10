# contoh_string.py
s = "halo dunia"
print("Asli:", s)

# hitung berapa kali 'a' muncul
print("'a' muncul sebanyak:", s.count('a'))

# ganti 'a' jadi 'A'
s2 = s.replace('a', 'A')
print("Setelah replace:", s2)

# ambil karakter ke-3 (index 2)
print("Karakter ke-3:", s[2])

#HASIL MODIFIKASI
# contoh_string_modifikasi.py

# input dari user
s = input("Masukkan sebuah kalimat: ")
print("Asli:", s)

# hitung huruf tertentu
huruf = input("Masukkan huruf yang ingin dihitung: ")
print(f"'{huruf}' muncul sebanyak:", s.count(huruf))

# ubah semua huruf kecil jadi besar
s_upper = s.upper()
print("Semua huruf diubah menjadi kapital:", s_upper)

# ambil karakter pertama dan terakhir
print("Karakter pertama:", s[0])
print("Karakter terakhir:", s[-1])

# membalik seluruh kalimat
print("Kalimat dibalik:", s[::-1])
