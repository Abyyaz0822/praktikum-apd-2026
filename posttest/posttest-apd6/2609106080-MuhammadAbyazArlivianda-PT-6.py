import os

pengguna = {
    "admin": {
        "password": "80",
        "jenis": "admin"
    }
}

koleksi_kartu = {
    1: {"nama": "UNO Merah", "warna": "Merah", "angka": 5, "jumlah": 2},
    2: {"nama": "UNO Biru", "warna": "Biru", "angka": 7, "jumlah": 3},
    3: {"nama": "UNO Hijau", "warna": "Hijau", "angka": 2, "jumlah": 4},
    4: {"nama": "UNO Putih", "warna": "Putih", "angka": 0, "jumlah": 1}
}

jalan = True

while jalan:
    os.system("cls" if os.name == "nt" else "clear")
    print("===================================")
    print("      SISTEM KOLEKSI KARTU UNO")
    print("===================================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("========== REGISTER ==========")
        username_baru = input("Buat username: ")
        password_baru = input("Buat password: ")

        if username_baru == "" or password_baru == "":
            print("Data tidak boleh kosong.")
        elif username_baru in pengguna:
            print("Username sudah digunakan.")
        else:
            pengguna[username_baru] = {
                "password": password_baru,
                "jenis": "pengguna"
            }
            print("Register berhasil!")
        input("Tekan Enter untuk kembali...")

    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("========== LOGIN ==========")
        username = input("Username: ")
        password = input("Password: ")

        if username not in pengguna or pengguna[username]["password"] != password:
            print("Username atau password salah.")
            input("Tekan Enter untuk kembali...")
        else:
            jenis_pengguna = pengguna[username].get("jenis")
            masuk_menu = True

            while masuk_menu:
                os.system("cls" if os.name == "nt" else "clear")
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
                        os.system("cls" if os.name == "nt" else "clear")
                        print("========== TAMBAH KARTU ==========")
                        nama = input("Nama kartu: ")
                        warna = input("Warna (Putih/Merah/Biru/Hijau): ")
                        angka = input("Angka kartu (0-9): ")
                        jumlah = input("Jumlah kartu: ")

                        angka_valid = True
                        if angka == "":
                            angka_valid = False
                        else:
                            for karakter in angka:
                                if karakter not in "0123456789":
                                    angka_valid = False

                        jumlah_valid = True
                        if jumlah == "":
                            jumlah_valid = False
                        else:
                            for karakter in jumlah:
                                if karakter not in "0123456789":
                                    jumlah_valid = False

                        if nama == "":
                            print("Nama tidak boleh kosong.")
                        elif warna not in ["Putih", "Merah", "Biru", "Hijau"]:
                            print("Warna kartu tidak valid.")
                        elif angka_valid == False or int(angka) > 9:
                            print("Angka harus dari 0 sampai 9.")
                        elif jumlah_valid == False:
                            print("Jumlah harus berupa angka.")
                        elif int(jumlah) <= 9:
                            print("Masukkan jumlah lebih dari 9.")
                        else:
                            nomor_baru = 1
                            for nomor in koleksi_kartu.keys():
                                if nomor >= nomor_baru:
                                    nomor_baru = nomor + 1

                            koleksi_kartu[nomor_baru] = {
                                "nama": nama,
                                "warna": warna,
                                "angka": int(angka),
                                "jumlah": int(jumlah)
                            }
                            print("Kartu berhasil ditambahkan!")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("========== DAFTAR KOLEKSI ==========")
                        if len(koleksi_kartu) == 0:
                            print("Koleksi masih kosong.")
                        else:
                            for nomor, kartu in koleksi_kartu.items():
                                print("-----------------------------------")
                                print("Nomor:", nomor)
                                print("Nama:", kartu.get("nama"))
                                print("Warna:", kartu.get("warna"))
                                print("Angka:", kartu.get("angka"))
                                print("Jumlah:", kartu.get("jumlah"))
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("========== UBAH DATA KARTU ==========")

                        if len(koleksi_kartu) == 0:
                            print("Koleksi masih kosong.")
                        else:
                            for nomor, kartu in koleksi_kartu.items():
                                print(nomor, kartu["nama"], kartu["warna"],
                                      kartu["angka"], kartu["jumlah"])

                            nomor_ubah = input("Nomor kartu yang diubah: ")
                            nomor_valid = True

                            if nomor_ubah == "":
                                nomor_valid = False
                            else:
                                for karakter in nomor_ubah:
                                    if karakter not in "0123456789":
                                        nomor_valid = False

                            if nomor_valid == False:
                                print("Nomor kartu harus berupa angka.")
                            elif int(nomor_ubah) not in koleksi_kartu:
                                print("Nomor kartu tidak tersedia.")
                            else:
                                nomor_ubah = int(nomor_ubah)
                                kartu = koleksi_kartu[nomor_ubah]

                                nama_baru = input("Nama baru (kosong = tetap): ")
                                warna_baru = input("Warna baru (kosong = tetap): ")
                                angka_baru = input("Angka baru (kosong = tetap): ")
                                jumlah_baru = input("Jumlah baru (kosong = tetap): ")

                                if nama_baru == "":
                                    nama_baru = kartu["nama"]
                                if warna_baru == "":
                                    warna_baru = kartu["warna"]
                                if angka_baru == "":
                                    angka_baru = str(kartu["angka"])
                                if jumlah_baru == "":
                                    jumlah_baru = str(kartu["jumlah"])

                                angka_valid = True
                                for karakter in angka_baru:
                                    if karakter not in "0123456789":
                                        angka_valid = False

                                jumlah_valid = True
                                for karakter in jumlah_baru:
                                    if karakter not in "0123456789":
                                        jumlah_valid = False

                                if nama_baru == "":
                                    print("Nama tidak boleh kosong.")
                                elif warna_baru not in ["Putih", "Merah", "Biru", "Hijau"]:
                                    print("Warna tidak valid.")
                                elif angka_valid == False or angka_baru == "" or int(angka_baru) > 9:
                                    print("Angka harus dari 0 sampai 9.")
                                elif jumlah_valid == False or jumlah_baru == "":
                                    print("Jumlah harus berupa angka.")
                                elif int(jumlah_baru) <= 0:
                                    print("Jumlah harus lebih dari 0.")
                                else:
                                    kartu.update({
                                        "nama": nama_baru,
                                        "warna": warna_baru,
                                        "angka": int(angka_baru),
                                        "jumlah": int(jumlah_baru)
                                    })
                                    print("Data berhasil diubah!")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("========== HAPUS KARTU ==========")

                        if len(koleksi_kartu) == 0:
                            print("Koleksi masih kosong.")
                        else:
                            for nomor, kartu in koleksi_kartu.items():
                                print(nomor, kartu["nama"], kartu["warna"],
                                      kartu["angka"], kartu["jumlah"])

                            nomor_hapus = input("Nomor kartu yang dihapus: ")
                            nomor_valid = True

                            if nomor_hapus == "":
                                nomor_valid = False
                            else:
                                for karakter in nomor_hapus:
                                    if karakter not in "0123456789":
                                        nomor_valid = False

                            if nomor_valid == False:
                                print("Nomor kartu harus berupa angka.")
                            elif int(nomor_hapus) in koleksi_kartu:
                                del koleksi_kartu[int(nomor_hapus)]
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
                        os.system("cls" if os.name == "nt" else "clear")
                        print("========== DAFTAR KOLEKSI ==========")
                        if len(koleksi_kartu) == 0:
                            print("Koleksi masih kosong.")
                        else:
                            for nomor, kartu in koleksi_kartu.items():
                                print("-----------------------------------")
                                print("Nomor:", nomor)
                                print("Nama:", kartu.get("nama"))
                                print("Warna:", kartu.get("warna"))
                                print("Angka:", kartu.get("angka"))
                                print("Jumlah:", kartu.get("jumlah"))
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
