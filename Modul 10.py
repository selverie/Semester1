import sqlite3
con = sqlite3.connext('mahasiswa.db')

cur = con.cursor()

cur.execute('''CREATE TABLE mahasiswa
                (NPM integer, Nama text, Fakultas Text, Program Studi text)''')

cur.execute("INSERT INTO mahasiswa VALUES (246, 'Kun', 'Sains dan Teknologi', 'Informatika')")

con.commit()
con.close()

'''
Simpan Database 
1. Pergi Ke Direktori Program 
2. cd sqlite3
3. python db.py
4. # database tersimpan
5. Buka DB Browser
'''