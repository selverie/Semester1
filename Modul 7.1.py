data_mahasiswa = []

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    asal = input("Masukkan Asal: ")
    data_mahasiswa.append({'NIM': nim, 'Nama': nama, 'Asal': asal})
    print("Data berhasil ditambahkan!")

def tampil_data():
    if not data_mahasiswa:
        print("Belum ada data yang ditambahkan")
    else:
        print("NIM\tNama\tAsal")
        for data in data_mahasiswa:
            print(f"{data['NIM']}\t{data['Nama']}\t{data['Asal']}")

def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    for data in data_mahasiswa:
        if data['NIM'] == nim:
            data_mahasiswa.remove(data)
            print("Data berhasil dihapus!")
            break
    else:
        print("Data tidak ditemukan")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        print("Program selesai, terima kasih!")
        break
    else:
        print("Pilihan salah, silahkan coba lagi")
