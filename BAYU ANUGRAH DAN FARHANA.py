import os
import time
from termcolor import colored

# Fungsi untuk menyambut pengguna
def pertama():
    print(colored('Selamat datang di Stasiun Kereta Api Sumatera Barat\n', 'cyan'))

    def welcome():
        awal = input('Apakah anda ingin melakukan pemesanan tiket kereta api (Y/T): ')
        if awal.upper() == 'Y':
            print(colored('Selamat Datang di Menu Pemesanan Tiket Kereta Api KAI Indonesia Sumatera Barat', 'green'))
        elif awal.upper() == 'T':
            quit()
        else:
            print(colored('Input yang Anda Masukkan Salah', 'red'))
            welcome()
    welcome()

    # Input nama dan nomor WhatsApp
    nama = input('Silahkan masukkan nama anda: ')
    print('Nama: ', nama)
    nomor = input('Silahkan Masukkan Nomor WhatsApp Anda: ')
    print('Nomor WhatsApp: ', nomor)

    # Menampilkan menu pemesanan tiket berdasarkan kelas
    print('Tiket Kereta Api berdasarkan Class')
    menuPemesanan = ['1. VIP', '2. Bisnis', '3. Ekonomi\n']
    for menu2 in menuPemesanan:
        print(menu2)

    # Fungsi untuk memilih kelas tiket
    def kelas():
        menuKelas = int(input('Silahkan Masukkan Angka Berdasarkan Tiket Kelas yang Tersedia: '))
        if menuKelas == 1:
            print(colored('Selamat Datang di VIP Class', 'blue'))
        elif menuKelas == 2:
            print(colored('Selamat Datang di Bisnis Class', 'blue'))
        elif menuKelas == 3:
            print(colored('Selamat Datang di Ekonomi Class', 'blue'))
        else:
            print(colored('Input yang Anda Masukkan Salah', 'red'))
            kelas()
    kelas()

    # Menampilkan metode pembayaran
    print('Metode untuk Pembayaran Tiket')
    metodePembayaran = ['1. Tunai', '2. Non Tunai\n']
    for menu3 in metodePembayaran:
        print(menu3)

    # Fungsi untuk memilih metode pembayaran
    def metode():
        metodePembayaran = int(input('Silahkan untuk Masukkan Angka Berdasarkan Metode Pembayaran: '))
        if metodePembayaran == 1:
            print(colored('Ambil struk pembayaran, bayar di loket KAI Indonesia Sumatera Barat', 'magenta'))
            print(colored('Terima kasih telah menyelesaikan pembelian tiket kereta api', 'green'))
            exit()
        elif metodePembayaran == 2:
            print(colored('Silahkan menyelesaikan pembayaran Anda', 'green'))
        else:
            print(colored('Input Anda Salah', 'red'))
            metode()

        uang = int(input('Silahkan memasukkan uang sebesar Rp.10.000,00: '))
        if uang >= 10000:
            hasil = uang - 10000
            print('Kembalian uang anda sebesar', hasil)
            print(colored('Pembayaran selesai, menampilkan tiket online', 'green'))
        else:
            print(colored('Mohon maaf uang anda tidak mencukupi', 'red'))
            metode()
    metode()

    # Memastikan apakah ada pembelian tiket lagi
    def last():
        again = input('Apakah anda ingin melakukan pembelian lagi (Y/T): ')
        if again.upper() == 'Y':
            pertama()
        elif again.upper() == 'T':
            print(colored('Terimakasih telah melakukan pemesanan tiket KAI Indonesia Sumatera Barat', 'cyan'))
            menu()
        else:
            print(colored('Input Anda Salah', 'red'))
            last()
    last()

# Definisikan jadwal kedatangan dan keberangkatan kereta api
jadwal_kereta = [
    ["Kereta", "Asal", "Tujuan", "Waktu Kedatangan", "Waktu Keberangkatan"],
    ["Kereta 1", "Padang", "Bukittinggi", "08:00", "08:30"],
    ["Kereta 2", "Padang", "Solok", "09:00", "09:30"],
    ["Kereta 3", "Padang", "Pariaman", "10:00", "12:20"],
    ["Kereta 4", "Padang", "Payakumbuh", "11:00", "11:30"],
]

# Fungsi untuk menampilkan jadwal kereta
def tampilkan_jadwal(jadwal):
    for baris in jadwal:
        print("{:<10} {:<15} {:<15} {:<20} {:<20}".format(*baris))

# Fungsi untuk memilih jadwal kereta api Sumatera Barat
def pilih_jadwal(jadwal):
    print("Pilih jadwal kereta:")
    for i in range(1, len(jadwal)):
        print(f"{i}. {jadwal[i][0]} dari {jadwal[i][1]} ke {jadwal[i][2]} - Kedatangan: {jadwal[i][3]}, Keberangkatan: {jadwal[i][4]}")

    pilihan = int(input("Masukkan nomor jadwal yang ingin dipilih: "))
    if 1 <= pilihan < len(jadwal):
        print("Anda memilih:")
        print("{:<10} {:<15} {:<15} {:<20} {:<20}".format(*jadwal[pilihan]))
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menampilkan jadwal kereta
print("Jadwal Kereta Api Sumatera Barat")
tampilkan_jadwal(jadwal_kereta)
pilih_jadwal(jadwal_kereta)

# Fungsi untuk menambahkan data penumpang
def tambah_data(data):
    with open("data.txt", "a") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
    print("Data berhasil disimpan!")

# Fungsi untuk menghapus data penumpang
def hapus_data_penumpang(nl):
    lines = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
    with open("data.txt", "w") as file:
        for i in lines:
            if i.split(",")[0] != nl:
                file.write(i)
    print("Data dihapus")

# Fungsi untuk mengedit data penumpang
def edit_data_penumpang(nl):
    lines = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
    with open("data.txt", "w") as file:
        for line in lines:
            if nl + "," in line:
                nb = input("Input nama baru: ")
                ttl = input("Input tanggal lahir: ")
                um = input("Input umur: ")
                jk = input("Jenis kelamin: ")
                nik = input("Nomor Induk Keluarga: ")
                file.write(f"{nb},{ttl},{um},{jk},{nik}\n")
            else:
                file.write(line)
    print("Data sudah diedit")

# Fungsi untuk menampilkan data penumpang
def tampilkan_data_penumpang():
    if os.path.exists("data.txt"):
        with open("data.txt", "r") as file:
            data = file.read()
        if data:
            print("Data penumpang:")
            print(data)
        else:
            print("Data penumpang tidak tersedia.")
    else:
        print("File data.txt tidak ditemukan.")

# Fungsi untuk menampilkan menu utama
def menu():
    while True:
        print(colored("====MENU UTAMA====", "red"))
        print("1. Tambahkan data penumpang")
        print("2. Hapus data penumpang")
        print("3. Edit data penumpang")
        print("4. Tampilkan data penumpang")
        print("5. Keluar")

        pilih = input("Pilih opsi (1/2/3/4/5): ")
        if pilih == "1":
            nl = input("Nama lengkap: ")
            ttl = input("Input tanggal lahir: ")
            um = input("Umur: ")
            jk = input("Jenis kelamin: ")
            nik = input("Nomor Induk Keluarga: ")
            data_penumpang = {
                "Nama Lengkap": nl,
                "Tanggal Lahir": ttl,
                "Umur": um,
                "Jenis Kelamin": jk,
                "Nomor Induk Keluarga": nik
            }
            tambah_data(data_penumpang)
        elif pilih == "2":
            nl = input("Nama yang dihapus: ")
            hapus_data_penumpang(nl)
        elif pilih == "3":
            nl = input("Nama yang diedit: ")
            edit_data_penumpang(nl)
        elif pilih == "4":
            tampilkan_data_penumpang()
        elif pilih == "5":
            print(colored("Terima kasih telah mengisi data penumpang", "green"))
            break
        else:
            print("Pilihan tidak valid")

# Memulai program
pertama()
menu()
