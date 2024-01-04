import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan1.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan ORDER BY
kursor.execute("SELECT * FROM HEWAN ORDER BY nama_hewan ASC") #ASC|DESC
baris_table = kursor.fetchall()

print("Data Hewan:")
print("="*110)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format("ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("-"*110)
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()