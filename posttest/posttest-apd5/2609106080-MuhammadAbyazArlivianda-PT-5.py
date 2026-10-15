import os

pengguna = [["admin", "80", "admin"]]
koleksi_kartu = [["UNO Merah", "Merah", 5, 2], ["UNO Biru", "Biru", 7, 3], ["UNO Hijau", "Hijau", 2, 4], ["UNO Putih", "Putih", 0, 1]]
jalan = True

while jalan:
    os.system("cls")
    print("===================================")
    print("      SISTEM KOLEKSI KARTU UNO")
    print("===================================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        os.system("cls")
        print("========== REGISTER ==========")
        username_baru = input("Buat username: ")
        password_baru = input("Buat password: ")
        if username_baru == "" or password_baru == "":
            print("Data tidak boleh kosong.")
        else:
            username_ada = False
            for akun in pengguna:
                if akun[0] == username_baru:
                    username_ada = True
            if username_ada == True:
                print("Username sudah digunakan.")
            else:
                pengguna.append([username_baru, password_baru, "pengguna"])
                print("Register berhasil!")
        input("Tekan Enter untuk kembali...")

    elif menu == "2":
        os.system("cls")
        print("========== LOGIN ==========")
        username = input("Username: ")
        password = input("Password: ")
        akun_ditemukan = False
        jenis_pengguna = ""

        for akun in pengguna:
            if akun[0] == username and akun[1] == password:
                akun_ditemukan = True
                jenis_pengguna = akun[2]

        if akun_ditemukan == False:
            print("Username atau password salah.")
            input("Tekan Enter untuk kembali...")
        else:
            masuk_menu = True
            while masuk_menu:
                os.system("cls")
                print("===================================")

                if jenis_pengguna == "admin":
                    print("MENU ADMIN")
                    print("1. Tambah kartu")
                    print("2. Lihat koleksi")
                    print("3. Ubah kartu")
                    print("4. Hapus kartu")
                    print("5. Logout")
                    pilihan = input("Pilih menu: ")

                    if pilihan == "1":
                        os.system("cls")
                        print("========== TAMBAH KARTU ==========")
                        nama = input("Nama kartu: ")
                        warna = input("Warna (Putih/Merah/Biru/Hijau): ")
                        angka = input("Angka kartu (0-9): ")
                        jumlah = input("Jumlah kartu: ")

                        if nama == "":
                            print("Nama tidak boleh kosong.")
                        elif warna != "Putih" and warna != "Merah" and warna != "Biru" and warna != "Hijau":
                            print("Warna kartu tidak valid.")
                        elif angka != "0" and angka != "1" and angka != "2" and angka != "3" and angka != "4" and angka != "5" and angka != "6" and angka != "7" and angka != "8" and angka != "9":
                            print("Angka harus dari 0 sampai 9.")
                        elif jumlah == "" or jumlah == "0" or jumlah == "1" or jumlah == "2" or jumlah == "3" or jumlah == "4" or jumlah == "5" or jumlah == "6" or jumlah == "7" or jumlah == "8" or jumlah == "9":
                            print("Masukkan jumlah lebih dari 9.")
                        else:
                            koleksi_kartu.append([nama, warna, int(angka), int(jumlah)])
                            print("Kartu berhasil ditambahkan!")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "2":
                        os.system("cls")
                        print("========== DAFTAR KOLEKSI ==========")
                        nomor = 1
                        for kartu in koleksi_kartu:
                            print("-----------------------------------")
                            print("Nomor:", nomor)
                            print("Nama:", kartu[0])
                            print("Warna:", kartu[1])
                            print("Angka:", kartu[2])
                            print("Jumlah:", kartu[3])
                            nomor = nomor + 1
                        if nomor == 1:
                            print("Koleksi masih kosong.")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "3":
                        os.system("cls")
                        print("========== UBAH DATA KARTU ==========")
                        nomor = 1
                        for kartu in koleksi_kartu:
                            print(nomor, kartu[0], kartu[1], kartu[2], kartu[3])
                            nomor = nomor + 1
                        nomor_ubah = input("Nomor kartu yang diubah: ")
                        nomor = 1
                        indeks = -1
                        for kartu in koleksi_kartu:
                            if str(nomor) == nomor_ubah:
                                indeks = nomor - 1
                            nomor = nomor + 1
                        if indeks != -1:
                            nama_baru = input("Nama baru: ")
                            warna_baru = input("Warna baru: ")
                            angka_baru = input("Angka baru: ")
                            jumlah_baru = input("Jumlah baru: ")
                            if nama_baru == "":
                                nama_baru = koleksi_kartu[indeks][0]
                            if warna_baru == "":
                                warna_baru = koleksi_kartu[indeks][1]
                            if angka_baru == "":
                                angka_baru = str(koleksi_kartu[indeks][2])
                            if jumlah_baru == "":
                                jumlah_baru = str(koleksi_kartu[indeks][3])
                            if warna_baru != "Putih" and warna_baru != "Merah" and warna_baru != "Biru" and warna_baru != "Hijau":
                                print("Warna tidak valid.")
                            elif angka_baru != "0" and angka_baru != "1" and angka_baru != "2" and angka_baru != "3" and angka_baru != "4" and angka_baru != "5" and angka_baru != "6" and angka_baru != "7" and angka_baru != "8" and angka_baru != "9":
                                print("Angka tidak valid.")
                            elif jumlah_baru == "" or jumlah_baru == "0":
                                print("Jumlah tidak valid.")
                            else:
                                koleksi_kartu[indeks][0] = nama_baru
                                koleksi_kartu[indeks][1] = warna_baru
                                koleksi_kartu[indeks][2] = int(angka_baru)
                                koleksi_kartu[indeks][3] = int(jumlah_baru)
                                print("Data berhasil diubah!")
                        else:
                            print("Nomor kartu tidak tersedia.")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "4":
                        os.system("cls")
                        print("========== HAPUS KARTU ==========")
                        nomor = 1
                        for kartu in koleksi_kartu:
                            print(nomor, kartu[0], kartu[1], kartu[2], kartu[3])
                            nomor = nomor + 1
                        nomor_hapus = input("Nomor kartu yang dihapus: ")
                        koleksi_baru = []
                        nomor = 1
                        kartu_ditemukan = False
                        for kartu in koleksi_kartu:
                            if str(nomor) == nomor_hapus:
                                kartu_ditemukan = True
                            else:
                                koleksi_baru.append(kartu)
                            nomor = nomor + 1
                        if kartu_ditemukan == True:
                            koleksi_kartu = koleksi_baru
                            print("Kartu berhasil dihapus!")
                        else:
                            print("Nomor kartu tidak tersedia.")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "5":
                        masuk_menu = False
                        print("Logout berhasil!")
                    else:
                        print("Pilihan tidak tersedia.")
                        input("Tekan Enter untuk lanjut...")

                else:
                    print("MENU PENGGUNA")
                    print("1. Lihat koleksi kartu")
                    print("2. Logout")
                    pilihan = input("Pilih menu: ")
                    if pilihan == "1":
                        os.system("cls")
                        print("========== DAFTAR KOLEKSI ==========")
                        nomor = 1
                        for kartu in koleksi_kartu:
                            print("-----------------------------------")
                            print("Nomor:", nomor)
                            print("Nama:", kartu[0])
                            print("Warna:", kartu[1])
                            print("Angka:", kartu[2])
                            print("Jumlah:", kartu[3])
                            nomor = nomor + 1
                        if nomor == 1:
                            print("Koleksi masih kosong.")
                        input("Tekan Enter untuk lanjut...")
                    elif pilihan == "2":
                        masuk_menu = False
                        print("Logout berhasil!")
                    else:
                        print("Pilihan tidak tersedia.")
                        input("Tekan Enter untuk lanjut...")

    elif menu == "3":
        jalan = False
        print("Terima kasih!")
    else:
        print("Pilihan tidak tersedia.")
        input("Tekan Enter untuk kembali...")

print("Program selesai.")