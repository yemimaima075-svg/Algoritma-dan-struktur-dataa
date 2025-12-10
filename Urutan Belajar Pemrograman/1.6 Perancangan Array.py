# membuat array (list)
buah = ["apel", "mangga", "jeruk", "pisang"]

# menampilkan seluruh isi array
print("Daftar Buah:", buah)

# menampilkan elemen berdasarkan index
print("Buah pertama:", buah[0])
print("Buah terakhir:", buah[-1])

# menambah elemen ke array
buah.append("anggur")
print("Setelah ditambah:", buah)

# menghapus elemen
buah.remove("mangga")
print("Setelah dihapus:", buah)

#hasil modifikasi
# membuat array (list)
buah = ["apel", "mangga", "jeruk", "pisang"]

# fungsi menampilkan array
def tampilkan_buah():
    print("Daftar Buah:", buah)

# fungsi menambah buah
def tambah_buah(nama):
    buah.append(nama)
    print(f'"{nama}" berhasil ditambahkan!')

# fungsi menghapus buah
def hapus_buah(nama):
    if nama in buah:
        buah.remove(nama)
        print(f'"{nama}" berhasil dihapus!')
    else:
        print(f'"{nama}" tidak ditemukan!')

# menampilkan seluruh isi array
tampilkan_buah()

# akses elemen berdasarkan index
print("Buah pertama:", buah[0])
print("Buah terakhir:", buah[-1])

# menambah buah baru
tambah_buah("anggur")
tampilkan_buah()

# menghapus buah tertentu
hapus_buah("mangga")
tampilkan_buah()
