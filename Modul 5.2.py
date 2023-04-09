pass_word = []                          
print('\n-----------------------------------------')
print('        Buat Username dan Password       ')
print('-----------------------------------------')

username = input("Masukkan Username : ") 
password = input('Masukkan Password : ')

def konfirmasi():
    konfirm = input('Konfirmasi Ulang Password : ')
    pass_word.append(konfirm)    
    if konfirm == password:
        print('Password Cocok')    
    else:
        print('Password Tidak Sesuai')
        konfirmasi()       
konfirmasi()

print('-----------------------------------------')
print('                  Login                  ')
print('-----------------------------------------')

def konfirmasi1():
    email1 = input('Masukkan Username : ')
    if email1 == username:
        pass
    else:
        print('Username Tidak Terdaftar')
        konfirmasi1()
konfirmasi1() 

passWord = input('Masukkan Password : ')
if passWord == password:
    print('Username dan Password benar')
    print('Berhasil Login')
else:
    print('Password Salah')
    print('Gagal Login')
    