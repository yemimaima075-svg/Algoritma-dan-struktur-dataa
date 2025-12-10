# array_2d_sederhana.py

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Isi Matriks:")
print(matriks)

print("Elemen baris 1 kolom 2:", matriks[0][1])  # hasil: 2
print("Elemen baris 3 kolom 3:", matriks[2][2])  # hasil: 9

#hasil modifikasi 
# array_2d_sederhana_modifikasi.py

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Isi Matriks (format rapi):")
for baris in matriks:
    print(baris)

# jumlah baris dan kolom
print("Jumlah baris:", len(matriks))
print("Jumlah kolom:", len(matriks[0]))

# akses elemen tertentu
print("Elemen baris 1 kolom 2:", matriks[0][1])
print("Elemen baris 3 kolom 3:", matriks[2][2])

# menampilkan elemen diagonal
print("Elemen diagonal utama:")
for i in range(len(matriks)):
    print(matriks[i][i])

# menjumlahkan semua elemen matriks
total = 0
for i in range(len(matriks)):
    for j in range(len(matriks[i])):
        total += matriks[i][j]

print("Total semua elemen:", total)
