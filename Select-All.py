import sqlite3

conn = sqlite3.connect('database_hewan1.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN")
rows = cursor.fetchall()

print("Data Hewan:")
print("==================================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format("ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Saat ini", "Tahun Ditemukan"))
print("--------------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 
conn.close()
