from data import koleksi_kartu, daftar_warna
from utilitas import bersihkan_layar, tekan_enter, pilih_menu
from utilitas import buat_nomor_baru, minta_warna, input_angka
from tampilan import cetak_judul, tampilkan_koleksi

def tambah_kartu():
    bersihkan_layar()
    cetak_judul("TAMBAH KARTU")
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
        tekan_enter()

def ubah_kartu():
    bersihkan_layar()
    cetak_judul("UBAH DATA KARTU")
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
    tekan_enter()

def hapus_kartu():
    bersihkan_layar()
    cetak_judul("HAPUS KARTU")
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
    tekan_enter()

def menu_admin():
    masuk_menu = True
    while masuk_menu:
        bersihkan_layar()
        cetak_judul("MENU ADMIN")
        pilihan = pilih_menu("Pilih menu admin", ["Tambah kartu", "Lihat koleksi", "Ubah kartu", "Hapus kartu", "Logout"])

        if pilihan == "Tambah kartu":
            tambah_kartu()
        elif pilihan == "Lihat koleksi":
            bersihkan_layar()
            cetak_judul("DAFTAR KOLEKSI")
            tampilkan_koleksi()
            tekan_enter()
        elif pilihan == "Ubah kartu":
            ubah_kartu()
        elif pilihan == "Hapus kartu":
            hapus_kartu()
        elif pilihan == "Logout":
            masuk_menu = False
            print("Logout berhasil!")