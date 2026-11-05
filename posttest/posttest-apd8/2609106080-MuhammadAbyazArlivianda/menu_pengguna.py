from utilitas import bersihkan_layar, tekan_enter, pilih_menu
from tampilan import cetak_judul, tampilkan_koleksi

def menu_pengguna():
    masuk_menu = True
    while masuk_menu:
        bersihkan_layar()
        cetak_judul("MENU PENGGUNA")
        pilihan = pilih_menu("Pilih menu pengguna", ["Lihat koleksi kartu", "Logout"])

        if pilihan == "Lihat koleksi kartu":
            bersihkan_layar()
            cetak_judul("DAFTAR KOLEKSI")
            tampilkan_koleksi()
            tekan_enter()
        elif pilihan == "Logout":
            masuk_menu = False
            print("Logout berhasil!")