def Penjumlahan ():
    print ("Penjumlahan")
    angka1 = float(input ("angka 1: "))
    angka2 = float(input ("angka 2: " ))
    print ("hasil = ",(angka1 + angka2))

def Pengurangan ():
    print ("Penjumlahan")
    angka1 = float(input ("angka 1: "))
    angka2 = float(input ("angka 2: " ))
    print ("hasil = ",(angka1 - angka2))

def Perkalian ():
    print ("Penjumlahan")
    angka1 = float(input ("angka 1: "))
    angka2 = float(input ("angka 2: " ))
    print ("hasil = ",(angka1 * angka2))

def Pembagian ():
    print ("Penjumlahan")
    angka1 = float(input ("angka 1: "))
    angka2 = float(input ("angka 2: " ))
    print ("hasil = ",(angka1 / angka2))

pilihan = int(input("Pilihan Tersedia :  \n 1. Penjumlahan \n 2. Pengurangan \n 3. Perkalian \n 4. Pembagian \n Pilihan = "))
if pilihan==1:
    Penjumlahan ()
elif pilihan==2:
    Pengurangan()
elif pilihan==3:
    Perkalian()
elif pilihan==4:
    Pembagian()
else:
    print("Pilihan Salah")