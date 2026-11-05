from data import pengguna
from utilitas import bersihkan_layar, tekan_enter
from tampilan import cetak_judul

def register():
    bersihkan_layar()
    cetak_judul("REGISTER")
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
        tekan_enter("Tekan Enter untuk kembali...")

def login():
    bersihkan_layar()
    cetak_judul("LOGIN")
    username = input("Username: ")
    password = input("Password: ")

    try:
        if username not in pengguna or pengguna[username]["password"] != password:
            raise ValueError("Username atau password salah.")
    except ValueError as e:
        print(e)
        tekan_enter("Tekan Enter untuk kembali...")
        return None
    else:
        return pengguna[username]["jenis"]