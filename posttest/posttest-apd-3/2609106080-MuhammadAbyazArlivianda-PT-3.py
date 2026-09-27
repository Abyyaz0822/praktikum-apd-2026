print("SELAMAT DATANG DI TOP UP STORE")

username = input("Username : ")
password = input("Password : ")

if username == "Abyaz" and password == "80":
    print("Login Berhasil!")
    
    id_player = input("ID Player : ")
    nama_game = input("Nama Game (Genshin Impact/Free Firee/Mobile Legends): ")

    print("=== KATEGORI TOP UP ===")
    print("1. Kecil    = Rp15.000")
    print("2. Menengah = Rp50.000")
    print("3. Besar    = Rp150.000")

    pilihan = input("Pilih kategori (1/2/3): ")

    if pilihan == "1":
        kategori = "Kecil"
        harga = 15000
    elif pilihan == "2":
        kategori = "Menengah"
        harga = 50000
    elif pilihan == "3":
        kategori = "Besar"
        harga = 150000
    else:
        print("Kategori tidak tersedia")
        exit()

    print("=== METODE PEMBAYARAN ===")
    print("1. Pulsa")
    print("2. E-Wallet")

    pembayaran = input("Pilih pembayaran (1/2): ")

    if pembayaran == "1":
        metode = "Pulsa"
    elif pembayaran == "2":
        metode = "E-Wallet"
    else:
        print("Metode pembayaran tidak tersedia")
        exit()

    admin = 2500 if metode == "Pulsa" else 500

    total_bayar = harga + admin

    print("TOTAL BAYAR : Rp", total_bayar)
    
    uang_bayar = int(input("Nominal Uang : Rp "))

    if uang_bayar < total_bayar:
        print("Transaksi Gagal Saldo tidak mencukupi")
    else:
        kembalian = uang_bayar - total_bayar

        print("          STRUK PEMBELIAN")
        print("ID Player       :", id_player)
        print("Nama Game       :", nama_game)
        print("Kategori        :", kategori)
        print("Metode Pembayaran:", metode)
        print("Biaya Admin     : Rp", admin)
        print("Total Bayar     : Rp", total_bayar)
        print("Uang Dibayar    : Rp", uang_bayar)
        print("Kembalian       : Rp", kembalian)
        print("=" * 40)
        print("     TRANSAKSI BERHASIL")
        print("=" * 40)

else:
    print("Login Gagal")