# quick_sort_sederhana.py

def quick_sort(data):
    # Jika panjang data 0 atau 1, langsung kembalikan (sudah terurut)
    if len(data) <= 1:
        return data
    
    # Pilih pivot (elemen pertama)
    pivot = data[0]

    # Bagi data menjadi 3 bagian
    kiri = [x for x in data[1:] if x < pivot]     # elemen lebih kecil
    kanan = [x for x in data[1:] if x >= pivot]   # elemen lebih besar atau sama

    # Rekursi: urutkan kiri + pivot + urutkan kanan
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)


# Data contoh
angka = [32, 11, 5, 90, 27, 15]

print("Data sebelum diurutkan :", angka)

# Panggil quick sort
hasil = quick_sort(angka)

print("Data setelah diurutkan :", hasil)

#hasil modifikasi 
# quick_sort_modifikasi.py

def quick_sort(data, level=0):
    indent = "  " * level
    print(f"{indent}Memproses: {data}")

    # Jika panjang data 0 atau 1 → sudah terurut
    if len(data) <= 1:
        print(f"{indent}Hasil: {data}")
        return data
    
    # Pivot dipilih dari elemen pertama
    pivot = data[0]
    print(f"{indent}Pivot: {pivot}")

    # Bagi data ke dua bagian
    kiri = [x for x in data[1:] if x < pivot]
    kanan = [x for x in data[1:] if x >= pivot]

    print(f"{indent}Kiri : {kiri}")
    print(f"{indent}Kanan: {kanan}")

    # Rekursi
    hasil = quick_sort(kiri, level + 1) + [pivot] + quick_sort(kanan, level + 1)

    print(f"{indent}Digabung: {hasil}")
    return hasil


# Input dari user
angka = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))

print("\nData sebelum diurutkan :", angka)

# Panggil quick sort
hasil = quick_sort(angka)

print("\nData setelah diurutkan :", hasil)
