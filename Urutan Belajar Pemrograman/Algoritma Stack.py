# stack_sederhana.py

# Membuat stack kosong
stack = []

print("=== Program Stack Sederhana ===")

# PUSH (menambah data)
stack.append("A")
stack.append("B")
stack.append("C")
print("Isi stack setelah push :", stack)

# POP (menghapus data paling atas)
terambil = stack.pop()
print("Data yang di-pop        :", terambil)

print("Isi stack sekarang      :", stack)

# Melihat elemen paling atas (top)
print("Elemen paling atas      :", stack[-1])

#hasil modifikasi
# stack_sederhana_modifikasi.py

stack = []

def tampilkan_stack():
    if len(stack) == 0:
        print("Stack kosong!")
    else:
        print("Isi stack :", stack)

print("=== Program Stack (Modifikasi) ===")

while True:
    print("\nMenu:")
    print("1. Push (tambah data)")
    print("2. Pop (hapus data)")
    print("3. Lihat elemen teratas")
    print("4. Tampilkan isi stack")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        stack.append(data)
        print(f"'{data}' berhasil ditambahkan.")

    elif pilihan == "2":
        if len(stack) == 0:
            print("Stack kosong, tidak bisa POP!")
        else:
            d = stack.pop()
            print("Data yang di-pop:", d)

    elif pilihan == "3":
        if len(stack) == 0:
            print("Stack kosong, tidak ada elemen teratas.")
        else:
            print("Elemen teratas:", stack[-1])

    elif pilihan == "4":
        tampilkan_stack()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
