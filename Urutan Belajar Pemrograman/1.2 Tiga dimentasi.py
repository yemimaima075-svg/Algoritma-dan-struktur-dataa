# array_3d_sederhana.py

kubus = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print("Isi Array 3D:")
print(kubus)

#hasil modifikasi
# array_3d_sederhana_modifikasi.py

kubus = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print("Isi Array 3D (ditampilkan per layer):")

# menampilkan isi array per layer
for i in range(len(kubus)):
    print(f"Layer {i}:")
    for baris in kubus[i]:
        print(baris)

# mengakses beberapa elemen
print("Contoh akses elemen:")
print("Elemen [0][0][1] =", kubus[0][0][1])  # hasil: 2
print("Elemen [1][1][0] =", kubus[1][1][0])  # hasil: 7

# menghitung jumlah semua elemen
total = 0
for i in range(len(kubus)):
    for j in range(len(kubus[i])):
        for k in range(len(kubus[i][j])):
            total += kubus[i][j][k]

print("Total semua elemen:", total)
