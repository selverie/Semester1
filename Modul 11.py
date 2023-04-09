def Penjumlaham(x, y):
    return x + y

def Pengurangan(x, y):
    return x - y

def Perkalian(x, y):
    return x * y

def Pembagian(x, y):
    return x / y

def Pangkat(x, y):
    return x ** y

def Akar(x, y):
    return x ** (1/y)

print("Pilih Operasi Matematika")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")
print("6. Akar")

pilih  = input("Pilih Antara (1/2/3/4/5/6) : ")

angka1 = int(input("Masukkan Angka Pertama : "))

angka2 = int(input("Masukkan Angka Kedua   : "))

if pilih == '1':
    print("Hasil =",angka1,"Di Tambah",angka2,"=", Penjumlaham(angka1, angka2))

elif pilih == '2':
    print("Hasil =",angka1,"Di Kurang",angka2,"=", Pengurangan(angka1, angka2))

elif pilih == '3':
    print("Hasil =",angka1,"Di Kali",angka2,"=", Perkalian(angka1, angka2))

elif pilih == '4':
    print("Hasil =",angka1,"Di Bagi",angka2,"=", Pembagian(angka1, angka2))
    
elif pilih == '5':
    print("Hasil =",angka1,"Pangkat",angka2,"=", Pangkat(angka1, angka2))
    
elif pilih == '6':
    print("Hasil =","Akar",angka1,"Pangkat",angka2,"=", Akar(angka1, angka2))

else:
    print("Pilihan Salah")