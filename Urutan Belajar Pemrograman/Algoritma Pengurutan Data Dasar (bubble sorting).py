# bubble_sort_sederhana.py

angka = [5, 2, 9, 1, 7]

print("Data sebelum diurutkan:", angka)

# Algoritma Bubble Sort
n = len(angka)
for i in range(n - 1):
    for j in range(n - i - 1):
        if angka[j] > angka[j + 1]:  # tukar posisi
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print("Data setelah diurutkan :", angka)

#hasil modifikasi
# bubble_sort_modifikasi.py

angka = [5, 2, 9, 1, 7]
print("Data awal:", angka)

# Memilih mode pengurutan
mode = input("Urutkan (a) Ascending / (d) Descending: ").lower()

n = len(angka)
print("\n=== Proses Bubble Sort ===")

for i in range(n - 1):
    print(f"\nIterasi ke-{i+1}:")
    for j in range(n - i - 1):
        print(f"  Bandingkan {angka[j]} dengan {angka[j+1]}")
        
        # Ascending
        if mode == "a" and angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]
            print("   -> Ditukar!")

        # Descending
        elif mode == "d" and angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]
            print("   -> Ditukar!")
        
        else:
            print("   -> Tidak ditukar")

print("\nData setelah diurutkan:", angka)
