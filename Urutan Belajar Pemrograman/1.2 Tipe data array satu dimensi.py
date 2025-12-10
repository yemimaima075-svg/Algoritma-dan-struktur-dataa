# array_sederhana.py

angka = [10, 20, 30, 40, 50]

print("Isi array:", angka)
print("Elemen pertama:", angka[0])
print("Elemen terakhir:", angka[-1])

#hasil modifikasi 
# array_sederhana_modifikasi.py

angka = [10, 20, 30, 40, 50]

print("Isi array:", angka)

# menampilkan jumlah elemen
print("Jumlah elemen:", len(angka))

# menampilkan elemen pertama & terakhir
print("Elemen pertama:", angka[0])
print("Elemen terakhir:", angka[-1])

# menampilkan elemen tengah
tengah = len(angka) // 2
print("Elemen tengah:", angka[tengah])

# menampilkan seluruh elemen satu per satu
print("Semua elemen:")
for x in angka:
    print("-", x)

# menampilkan nilai terbesar dan terkecil
print("Nilai terbesar:", max(angka))
print("Nilai terkecil:", min(angka))
