import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan1.db')
cursor = conn.cursor()

# Menjalankan query DELETE
jenis = 'Mamalia'  # ID pegawai yang akan dihapus
cursor.execute(f"DELETE FROM HEWAN WHERE jenis = ?", (jenis,))
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data pegawai dengan ID {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data pegawai dengan ID {jenis}.")

# Menutup koneksi
conn.close()
