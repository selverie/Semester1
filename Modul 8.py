print("\n---------------------------------")
print("              KASIR              ")
print("---------------------------------")
pembeli = input("Masukkan Nama Pembeli : ")
print("Nama Pembeli : ", pembeli)
print("---------------------------------") 

def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    print("\n---------------------------------") 
    print("            Menu Makanan           ")
    print("---------------------------------")  
    print("1. Nasi Goreng - Rp 14000")
    print("2. Mie Goreng - Rp 9000")
    print("3. Mie Kuah - Rp 10000")
    nomor=int(input("Masukan Pilihan : "))
    porsi=int(input("Berapa Porsi : "))
    
    if nomor==1:
        totalmkn=porsi*15000
        print(porsi," porsi Nasi Goreng = Rp", totalmkn)
        mkn=("Nasi Goreng")
    elif nomor==2:
        totalmkn=porsi*9000
        print(porsi," porsi Mie Goreng = Rp", totalmkn)
        mkn=("Soto")
    elif nomor==3:
        totalmkn=porsi*11000
        print(porsi, " porsi Mie Kuah = Rp", totalmkn)
        mkn=("Mie Ayam")
    else:
        print("Pilihan Tidak Tersedia, Coba Yang Lain!")
        fungsimakanan()

def fungsiminuman():
    global totalmnm
    global mnm
    global gelas
    print("\n---------------------------------") 
    print("            Menu Minuman           ")
    print("---------------------------------")  
    print("1. Es Teh - Rp 3000")
    print("2. Es Jeruk - Rp 4000")
    print("3. Es Kopi - Rp 5000")
    nomor=int(input("Masukan Pilihan : "))
    gelas= int(input("Berapa Gelas : "))

    if nomor==1:
        totalmnm=gelas*2000
        print (gelas," Es Teh = Rp", totalmnm)
        mnm=(" Gelas Es Teh")
    elif nomor==2:
        totalmnm=gelas*3500
        print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
        mnm=("Es Jeruk")
    elif nomor==3:
        totalmnm=gelas*4000
        print (gelas, " Gelas Es Kopi = Rp", totalmnm)
        mnm=("Es Kopi")
    else:
        print("Pilihan Tidak Tersedia, Coba Yang Lain!")
        fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar : Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli : Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n---------------------------------") 
print("---------STRUK--PEMBELIAN--------")
print("---------------------------------")  
print("Nama\t\t:",pembeli)
print("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print("Tagihan\t\t: Rp",totalsemua)
print("Dibayar\t\t: Rp",uang)
print("Kembalian\t: Rp",kembalian)
print("---------------------------------")  
print("---------------------------------")  