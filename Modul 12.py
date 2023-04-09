Nama = input("\nMasukkan Nama : ")
NPM = input("Masukkan NPM : ")
Matkul = input("Masukkan Mata Kuliah : ")
Quiz = float(input("Masukkan Nilai Quiz : "))
Tugas = float(input("Masukkan Nilai Tugas : "))
UTS = float(input("Masukkan Nilai UTS : "))
UAS = float(input("Masukkan Nilai UAS : "))

NilaiQuiz = int(Quiz * 20/100)
NilaiTugas = int(Tugas * 25/100)
NilaiUTS = int(UTS * 25/100)
NilaiUAS = int(UAS * 30/100)

NilaiAkhir = NilaiQuiz + NilaiTugas + NilaiUTS + NilaiUAS

print("\nNama : "+Nama)
print("Nim : "+NPM)
print("Matkul : "+Matkul)
print("Nilai Akhir : ", int(NilaiAkhir))

if NilaiAkhir >= 90:
    print("Grade : A")
elif NilaiAkhir >= 80:
    print("Grade : B")
elif NilaiAkhir >= 70:
    print("Grade : C")
elif NilaiAkhir >= 50:
    print("Grade : D")
elif NilaiAkhir >= 40:
    print("Grade : E")

if NilaiAkhir >= 60:
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")