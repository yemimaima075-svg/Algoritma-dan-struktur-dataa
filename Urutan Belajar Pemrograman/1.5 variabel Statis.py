class Motor:
    # Variabel statis
    jumlah_motor = 0

    def __init__(self, merk):
        self.merk = merk
        # setiap membuat objek baru, jumlah_motor bertambah
        Motor.jumlah_motor += 1

# membuat objek
m1 = Motor("Honda")
m2 = Motor("Yamaha")

print("Motor 1:", m1.merk)
print("Motor 2:", m2.merk)

# mengakses variabel statis
print("Total motor:", Motor.jumlah_motor)

#hasil modifikasi
class Motor:
    # Variabel statis
    jumlah_motor = 0

    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
        # tiap objek dibuat, jumlah_motor bertambah
        Motor.jumlah_motor += 1

    def info(self):
        return f"Merk: {self.merk}, Warna: {self.warna}"

# membuat objek
m1 = Motor("Honda", "Merah")
m2 = Motor("Yamaha", "Hitam")
m3 = Motor("Suzuki", "Biru")

# menampilkan informasi setiap motor
print("Data Motor:")
print(m1.info())
print(m2.info())
print(m3.info())

# mengakses variabel statis
print("Total motor terdaftar:", Motor.jumlah_motor)
