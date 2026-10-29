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

daftar_warna = ["Putih", "Merah", "Biru", "Hijau"]

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_koleksi():
    if len(koleksi_kartu) == 0:
        print("Koleksi masih kosong.")
    else:
        for nomor, kartu in koleksi_kartu.items():
            print("-----------------------------------")
            print("Nomor:", nomor)
            print("Nama:", kartu["nama"])
            print("Warna:", kartu["warna"])
            print("Angka:", kartu["angka"])
            print("Jumlah:", kartu["jumlah"])
        print("-----------------------------------")
        total = hitung_total_rekursif(list(koleksi_kartu.keys()), 0)
        print("Total seluruh kartu:", total)

def buat_nomor_baru():
    nomor_baru = 1
    for nomor in koleksi_kartu.keys():
        if nomor >= nomor_baru:
            nomor_baru = nomor + 1
    return nomor_baru

def minta_warna():
    warna = input("Warna (Putih/Merah/Biru/Hijau): ")
    if warna not in daftar_warna:
        raise ValueError("Warna kartu tidak valid.")
    return warna

def input_angka(pesan, batas_min, batas_maks, nilai_lama=None):
    # nilai_lama dipakai saat ubah data: input kosong = nilai tetap
    teks = input(pesan)
    try:
        if nilai_lama is not None and teks == "":
            return nilai_lama
        nilai = int(teks)
    except ValueError:
        print("Input yang anda masukkan bukan Integer (angka).")
        return -1
    else:
        try:
            if nilai < batas_min or nilai > batas_maks:
                raise ValueError("Angka harus dari " + str(batas_min) + " sampai " + str(batas_maks) + ".")
        except ValueError as e:
            print(e)
            return -1
        else:
            return nilai

def hitung_total_rekursif(daftar_nomor, indeks):
    if indeks == len(daftar_nomor):
        return 0
    nomor = daftar_nomor[indeks]
    return koleksi_kartu[nomor]["jumlah"] + hitung_total_rekursif(daftar_nomor, indeks + 1)

jalan = True  

while jalan:
    bersihkan_layar()
    print("===================================")
    print("      SISTEM KOLEKSI KARTU UNO")
    print("===================================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        bersihkan_layar()
        print("========== REGISTER ==========")
        username_baru = input("Buat username: ")
        password_baru = input("Buat password: ")

        try:
            if username_baru == "" or password_baru == "":
                raise ValueError("Data tidak boleh kosong.")
            if username_baru in pengguna:
                raise ValueError("Username sudah digunakan.")
        except ValueError as e:
            print(e)
        else:
            pengguna[username_baru] = {
                "password": password_baru,
                "jenis": "pengguna"
            }
            print("Register berhasil!")
        finally:
            input("Tekan Enter untuk kembali...")

    elif menu == "2":
        bersihkan_layar()
        print("========== LOGIN ==========")
        username = input("Username: ")
        password = input("Password: ")

        try:
            if username not in pengguna or pengguna[username]["password"] != password:
                raise ValueError("Username atau password salah.")
        except ValueError as e:
            print(e)
            input("Tekan Enter untuk kembali...")
        else:
            jenis_pengguna = pengguna[username]["jenis"]
            masuk_menu = True

            while masuk_menu:
                bersihkan_layar()
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
                        bersihkan_layar()
                        print("========== TAMBAH KARTU ==========")
                        try:
                            nama = input("Nama kartu: ")
                            if nama == "":
                                raise ValueError("Nama tidak boleh kosong.")
                            warna = minta_warna()
                            angka = input_angka("Angka kartu (0-9): ", 0, 9)
                            if angka == -1:
                                raise ValueError("Kartu batal ditambahkan.")
                            jumlah = input_angka("Jumlah kartu (lebih dari 9): ", 10, 999999)
                            if jumlah == -1:
                                raise ValueError("Kartu batal ditambahkan.")
                        except ValueError as e:
                            print(e)
                        else:
                            koleksi_kartu[buat_nomor_baru()] = {
                                "nama": nama,
                                "warna": warna,
                                "angka": angka,
                                "jumlah": jumlah
                            }
                            print("Kartu berhasil ditambahkan!")
                        finally:
                            input("Tekan Enter untuk lanjut...")

                    elif pilihan == "2":
                        bersihkan_layar()
                        print("========== DAFTAR KOLEKSI ==========")
                        tampilkan_koleksi()
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "3":
                        bersihkan_layar()
                        print("========== UBAH DATA KARTU ==========")
                        if len(koleksi_kartu) == 0:
                            print("Koleksi masih kosong.")
                        else:
                            tampilkan_koleksi()
                            nomor_ubah = input_angka("Nomor kartu yang diubah: ", 1, 999999)

                            if nomor_ubah != -1:
                                try:
                                    if nomor_ubah not in koleksi_kartu:
                                        raise ValueError("Nomor kartu tidak tersedia.")
                                except ValueError as e:
                                    print(e)
                                else:
                                    kartu = koleksi_kartu[nomor_ubah]
                                    nama_baru = input("Nama baru (kosong = tetap): ")
                                    warna_baru = input("Warna baru (kosong = tetap): ")
                                    angka_baru = input_angka("Angka baru (kosong = tetap): ", 0, 9, kartu["angka"])
                                    jumlah_baru = input_angka("Jumlah baru (kosong = tetap): ", 1, 999999, kartu["jumlah"])

                                    if nama_baru == "":
                                        nama_baru = kartu["nama"]
                                    if warna_baru == "":
                                        warna_baru = kartu["warna"]

                                    try:
                                        if warna_baru not in daftar_warna:
                                            raise ValueError("Warna tidak valid.")
                                        if angka_baru == -1 or jumlah_baru == -1:
                                            raise ValueError("Data tidak jadi diubah.")
                                    except ValueError as e:
                                        print(e)
                                    else:
                                        kartu.update({
                                            "nama": nama_baru,
                                            "warna": warna_baru,
                                            "angka": angka_baru,
                                            "jumlah": jumlah_baru
                                        })
                                        print("Data berhasil diubah!")
                        input("Tekan Enter untuk lanjut...")

                    elif pilihan == "4":
                        bersihkan_layar()
                        print("========== HAPUS KARTU ==========")
                        if len(koleksi_kartu) == 0:
                            print("Koleksi masih kosong.")
                        else:
                            tampilkan_koleksi()
                            nomor_hapus = input_angka("Nomor kartu yang dihapus: ", 1, 999999)

                            if nomor_hapus != -1:
                                try:
                                    if nomor_hapus not in koleksi_kartu:
                                        raise ValueError("Nomor kartu tidak tersedia.")
                                except ValueError as e:
                                    print(e)
                                else:
                                    del koleksi_kartu[nomor_hapus]
                                    print("Kartu berhasil dihapus!")
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
                        bersihkan_layar()
                        print("========== DAFTAR KOLEKSI ==========")
                        tampilkan_koleksi()
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