class Siswa:
    def __init__(self, nama, nilai):
        # variabel dinamis (berbeda tiap objek)
        self.nama = nama
        self.nilai = nilai

# membuat objek
s1 = Siswa("marna", 85)
s2 = Siswa("kristia", 92)

# menampilkan data
print("Siswa 1:", s1.nama, "- Nilai:", s1.nilai)
print("Siswa 2:", s2.nama, "- Nilai:", s2.nilai)

#hasil modifikasi 
class Siswa:
    def __init__(self, nama, nilai):
        # variabel dinamis (berbeda tiap objek)
        self.nama = nama
        self.nilai = nilai

    def info(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def update_nilai(self, nilai_baru):
        self.nilai = nilai_baru

# membuat objek
s1 = Siswa("marna", 85)
s2 = Siswa("kristia", 92)

# update nilai salah satu siswa
s1.update_nilai(90)

# menampilkan data
print("Data Siswa:")
print(s1.info())
print(s2.info())
