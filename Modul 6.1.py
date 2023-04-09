#Algoritma Program
#1. Start
#2. 2.1 Declare SKS
#   2.2 Declare Nilai
#   2.3 Declare Bobot
#   2.4 Declare jumlah SKS
#   2.5 Declare jumlah Bobot
#   2.6 Declare hasil 
#   2.7 Declare IPK
#   2.8 Declare Integer = 10
#3. Input jumlah SKS
#4. hasil jumlah SKS = SKS + SKS + SKS + SKS
#5. Display hasil jumlah SKS
#6. Input IPK
#7. hasil IPK = (SKS x Nilai) 
#   7.1       = Bobot  
#   7.2       = jumlah Bobot/10
#8. Display hasil IPK 
#9. End

print("\n----------------------------------------------------------")
print("NAMA MK         | SKS |  | Nilai |  | Bobot(SKS x Nilai) |")
print("----------------------------------------------------------")
print("AGAMA           |  2  |  |   A   |  |      2x4=8         |")
print("----------------------------------------------------------")
print("Matematika      |  3  |  |   A   |  |      3x4=12        |")
print("----------------------------------------------------------")
print("Algoritma       |  3  |  |   C   |  |      3x2=6         |")
print("----------------------------------------------------------")
print("Pemrograman Web |  2  |  |   B   |  |      2x3=6         |")
print("----------------------------------------------------------")
print("                |  10 |  |       |  |        36          |")

import pandas as pd
import numpy as np

#Jumlah SKS
data = [2, 3, 3, 2]
df = pd.DataFrame(data)
df[0] = df[0].astype(int)
print("Jumlah SKS =", df[0].sum())

#SKS x Nilai
arr1 = np.array([2, 3, 3, 2])
arr2 = np.array([4, 4, 2, 3])

newarr = np.multiply(arr1, arr2)
print("Hasil SKS x Nilai = ", newarr)

#Bobot Keseluruhan
data = (newarr)
df = pd.DataFrame(data)
df[0] = df[0].astype(int)
print("Bobot Keseluruhan =", df[0].sum())

#IPK rata-rata
arr4 = np.array([10])
newarr = np.divide(df[0].sum(), arr4)
print("IPK rata-rata (Bobot : 10) =", newarr)
