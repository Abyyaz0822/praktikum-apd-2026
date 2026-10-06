print("SELAMAT DATANG DI BRI")

username_benar = "Abyaz"
pin_benar = "080"

saldo = 1000000

percobaan = 0
login_berhasil = False

while percobaan < 3:
    print("Login ATM")
    username = input("username: ")
    pin = input("pin: ")

    if username == username_benar and pin == pin_benar:
        print("Login Berhasil")
        login_berhasil = True
        break
    else:
        percobaan = percobaan + 1
        sisa = 3 - percobaan

        if sisa > 0:
            print("Login Gagal, sisa percobaan:", sisa)
        else:
            print("Akun Anda Terblokir")

if login_berhasil:
    while True:
        print()
        print("Menu ATM")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")

        pilihan = input("Masukkan Pilihan Anda (1-4): ")

        if pilihan == "1":
            print()
            print("CEK SALDO")
            print("Saldo Anda Rp", saldo)

        elif pilihan == "2":
            print()
            print("TARIK TUNAI")
            print("Pilih Kelipatan:")
            print("[1] Rp 50.000")
            print("[2] Rp 100.000")

            pilihan_kelipatan = input("Pilihan: ")
            nominal = int(input("Nominal Tarik: Rp "))

            if nominal <= 0:
                print("Nominal Harus Lebih Dari 0")

            elif pilihan_kelipatan == "1":
                if nominal % 50000 != 0:
                    print("Nominal Harus Kelipatan Rp 50.000")
                elif nominal > saldo:
                    print("Saldo Tidak Mencukupi")
                else:
                    saldo = saldo - nominal
                    print("Transaksi Berhasil")
                    print("Nominal Ditarik: Rp", nominal)
                    print("Sisa Saldo: Rp", saldo)

            elif pilihan_kelipatan == "2":
                if nominal % 100000 != 0:
                    print("Nominal Harus Kelipatan Rp 100.000")
                elif nominal > saldo:
                    print("Saldo Tidak Mencukupi")
                else:
                    saldo = saldo - nominal
                    print("Transaksi Berhasil")
                    print("Nominal Ditarik: Rp", nominal)
                    print("Sisa Saldo: Rp", saldo)

            else:
                print("Pilihan Kelipatan Tidak Valid")

        elif pilihan == "3":
            print()
            print("SETOR TUNAI")

            nominal = int(input("Nominal Setor: Rp "))

            if nominal <= 0:
                print("Nominal Setor Harus Lebih Dari 0")
            elif nominal % 50000 != 0:
                print("Nominal Setor Harus Kelipatan Rp 50.000")
            else:
                saldo = saldo + nominal
                print("Transaksi Berhasil")
                print("Nominal Disetor: Rp", nominal)
                print("Saldo Anda Sekarang: Rp", saldo)

        elif pilihan == "4":
            print()
            print("Terima Kasih Telah Menggunakan ATM BRI")
            print("Silahkan Datang Kembali")
            break

        else:
            print("Pilihan Tidak Valid")