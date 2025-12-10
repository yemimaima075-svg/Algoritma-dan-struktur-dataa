# shell_sort_sederhana.py

angka = [23, 12, 1, 8, 34, 54, 2, 3]

print("=== Algoritma Shell Sort Sederhana ===")
print("Data sebelum diurutkan:", angka)

n = len(angka)
gap = n // 2   # langkah awal gap

# Algoritma Shell Sort
while gap > 0:
    for i in range(gap, n):
        temp = angka[i]
        j = i

        # Geser elemen sesuai jarak gap
        while j >= gap and angka[j - gap] > temp:
            angka[j] = angka[j - gap]
            j -= gap

        angka[j] = temp

    print(f"Setelah gap {gap}: {angka}")
    gap //= 2  # perkecil gap

print("\nData setelah diurutkan :", angka)

#hasil modifikasi 
# shell_sort_modifikasi.py

def shell_sort(data):
    n = len(data)
    gap = n // 2
    langkah = 1

    print("=== Algoritma Shell Sort (Modifikasi) ===")
    print("Data awal:", data)

    # Proses Shell Sort
    while gap > 0:
        print(f"\n--- Langkah {langkah}: Gap = {gap} ---")
        
        for i in range(gap, n):
            temp = data[i]
            j = i

            # Geser elemen sesuai gap
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp
        
        print("Hasil sementara:", data)
        gap //= 2
        langkah += 1

    return data


# Data contoh
angka = [23, 12, 1, 8, 34, 54, 2, 3]

# Panggil fungsi
hasil = shell_sort(angka)

print("\n=== Hasil Akhir ===")
print("Data setelah diurutkan:", hasil)
