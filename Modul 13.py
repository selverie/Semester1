import sys 
total = []

print("--------------------------")
print("           KASIR          ")
print("--------------------------")

def daftar_barang():
    print(" No | Nama Barang | Harga")
    print("--------------------------")
    print(" 1  | Nasi Goreng | 15.000")
    print(" 2  | Nasi Padang | 25.000")
    print(" 3  | Nasi Bakar  | 20.000")
    print(" 4  | Es Jeruk    | 10.000")
    print(" 5  | Es Buah     | 15.000")
    print("--------------------------")
    kode = int(input("Masukkan Angka Barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan Jumlah Barang : "))
        total1 = 23000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan Jumlah Barang : "))
        total2 = 41200 * jumlah2
        total.append(total2)
        tanya() 
    elif kode == 3:
        jumlah3 = int(input("Masukkan Jumlah Barang : "))
        total3 = 59000 * jumlah3
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan Jumlah Barang : "))
        total4 = 23000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan Jmlah Barang  : "))
        total5 = 70000 * jumlah5
        total.append(total5)
        tanya()
        
def tanya():
    print("\n------------------------------")
    tanya = input("Ingin Tambah Barang? [y/t] : ")
    print("------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else: 
        print ("Pilihan yang anda masukan salah!")
        
def akhir():
    for harga in total:
        print("\n-----------------------------")
        print("             STRUK           ")
        print("-----------------------------")
        print("Subtotal       : Rp.", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100 
        elif a > 300000:
            diskon = a * 5/100 
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100 
        else:
            diskon = 0 
        print("Potongan Harga : Rp.", diskon)
        totalakhir = a - diskon
        print("Total          : Rp.", totalakhir)
        print("-----------------------------")   
        bayar = int(input("Bayar          : Rp. "))
        kembalian = bayar - totalakhir
        print("Kembalian      : Rp.", kembalian)
        print("----------------------------")
        print("        Terima Kasih        ")
        print("----------------------------")
        break
        
daftar_barang()    