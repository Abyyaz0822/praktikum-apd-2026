from importlib import import_module

from autentikasi import register, login
from utilitas import bersihkan_layar, pilih_menu
from tampilan import cetak_judul

def menu_admin():
    try:
        modul_admin = import_module("menu_admin")
    except ModuleNotFoundError:
        print("Modul menu_admin tidak ditemukan.")
        return

    modul_admin.menu_admin()

def menu_pengguna():
    try:
        modul_pengguna = import_module("menu_pengguna")
    except ModuleNotFoundError:
        print("Modul menu_pengguna tidak ditemukan.")
        return

    modul_pengguna.menu_pengguna()

def arahkan_menu(jenis_pengguna):
    # jenis_pengguna bernilai None jika login gagal
    if jenis_pengguna == "admin":
        menu_admin()
    elif jenis_pengguna == "pengguna":
        menu_pengguna()


def main():
    jalan = True

    while jalan:
        bersihkan_layar()
        cetak_judul("SISTEM KOLEKSI KARTU UNO")
        menu = pilih_menu("Pilih menu", ["Register", "Login", "Keluar"])

        if menu == "Register":
            register()
        elif menu == "Login":
            jenis = login()
            arahkan_menu(jenis)
        elif menu == "Keluar":
            jalan = False
            print("Terima kasih!")

    print("Program selesai.")


if __name__ == "__main__":
    main()