# selection_sort_sederhana.py

angka = [5, 2, 9, 1, 7]

print("Data sebelum diurutkan:", angka)

n = len(angka)

# Algoritma Selection Sort
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if angka[j] < angka[min_index]:
            min_index = j
    
    # Tukar nilai terkecil ke posisi i
    angka[i], angka[min_index] = angka[min_index], angka[i]

print("Data setelah diurutkan :", angka)

#hasil modifikasi
# selection_sort_modifikasi.py

# Meminta input data dari pengguna
angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))

print("\nData sebelum diurutkan:", angka)

n = len(angka)

# Algoritma Selection Sort dengan tampilan proses
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if angka[j] < angka[min_index]:
            min_index = j
    
    # Tukar nilai terkecil ke posisi i
    angka[i], angka[min_index] = angka[min_index], angka[i]

    # Menampilkan proses setiap langkah
    print(f"Langkah {i+1}: {angka}")

print("\nData setelah diurutkan:", angka)
