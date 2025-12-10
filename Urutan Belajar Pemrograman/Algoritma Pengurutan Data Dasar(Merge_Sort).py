# merge_sort_sederhana.py

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2       # titik tengah
        kiri = data[:mid]          # bagian kiri
        kanan = data[mid:]         # bagian kanan

        # Rekursi untuk mengurutkan tiap bagian
        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0

        # Proses penggabungan (merge)
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        # Jika masih ada elemen tersisa di kiri
        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        # Jika masih ada elemen tersisa di kanan
        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1


# Data contoh
angka = [38, 27, 43, 3, 9, 82, 10]

print("Data sebelum diurutkan:", angka)

# Panggil merge sort
merge_sort(angka)

print("Data setelah diurutkan :", angka)

#hasil modifikasi
# merge_sort_modifikasi.py

def merge_sort(data, level=0):
    print("  " * level + f"Memproses: {data}")

    if len(data) > 1:
        mid = len(data) // 2
        kiri = data[:mid]
        kanan = data[mid:]

        # Rekursi
        merge_sort(kiri, level + 1)
        merge_sort(kanan, level + 1)

        i = j = k = 0

        # Proses merge
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        # Sisa kiri
        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        # Sisa kanan
        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

    print("  " * level + f"Hasil:     {data}")


# Input dari user
angka = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))

print("\nData sebelum diurutkan:", angka)

merge_sort(angka)

print("\nData setelah diurutkan :", angka)
