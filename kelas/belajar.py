print("Welcome To Abyaz Top Up Store")

username_benar = "Kuzan"
password = "Kuzan 2008@"

percobaan = 0
login_berhasil = False

while percobaan < 3:
    print("Login")
    username = input("username: ")
    pin = input("Pin: ")

    if username == username_benar and pin == password:
        print("Login Berhasil")
        login_berhasil = True
        break
    else: 
        percobaan = percobaan + 1
        sisa = 3 - percobaan

        if sisa > 0:
            print("Login Gagal, sisa percobaan:", sisa)
        else:
            print("Password Salah")

if login_berhasil:
    while True:
        print()
        print("Menu Top Up")
        print("1. Mobile Legend")
        print("2. Free Firee")
        print("3. Pubg Mobile")
        print("4. Keluar")

        