a = input("Masukkan Huruf atau Angka : ")
b = c = 0

for x in a:
        if (x.isalpha()):
            b = b + 1

        elif (x.isdigit()):
            c = c + 1

print("jumlah huruf = ", b)
print("jumlah angka = ", c)
print("jumlah huruf dan angka = ", b + c )