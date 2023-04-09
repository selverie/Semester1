# Menghitung Luas Bangun

# Menghitung Luas Persegi Panjang
print("Menghitung Luas Persegi Panjang")

panjang = float(input("Masukkan Panjang : "))
lebar = float(input("Masukkan Lebar : "))

luasPersegiPanjang = panjang* lebar

print("Luas Persegi Panjang : ",luasPersegiPanjang)

# Menghitung Luas Setengah Lingkaran
print("\nMenghitung Luas Setengah Lingkaran")

PI = float(input("Masukkan PI : "))
diameter = float(input("Masukkan Diameter : "))

jariJari = diameter / 2

luasSetengahLingkaran = PI * jariJari * jariJari
print("Luas Setengah Lingkaran : ",luasSetengahLingkaran)

# Menghitung Luas Bangun
print("\nMenghitung Luas Bangun")

luasBangun = luasPersegiPanjang + luasSetengahLingkaran

print("Luas Bangun : ",luasBangun)

