# insertion_sort_sederhana.py

angka = [5, 2, 9, 1, 7]

print("Data sebelum diurutkan:", angka)

# Algoritma Insertion Sort
for i in range(1, len(angka)):
    key = angka[i]
    j = i - 1

    # Geser elemen yang lebih besar ke kanan
    while j >= 0 and angka[j] > key:
        angka[j + 1] = angka[j]
        j -= 1
    
    # Tempatkan key pada posisi yang benar
    angka[j + 1] = key

print("Data setelah diurutkan :", angka)

#hasil modifikasi
# insertion_sort_modifikasi.py

angka = [5, 2, 9, 1, 7]

print("=== Algoritma Insertion Sort Sederhana ===")
print("Data sebelum diurutkan:", angka)

# Algoritma Insertion Sort
for i in range(1, len(angka)):
    key = angka[i]
    j = i - 1

    # Geser elemen lebih besar ke kanan
    while j >= 0 and angka[j] > key:
        angka[j + 1] = angka[j]
        j -= 1

    # Tempatkan key pada posisi benar
    angka[j + 1] = key

    # Menampilkan proses per langkah
    print(f"Langkah {i}: {angka}")

print("\nData setelah diurutkan :", angka)
