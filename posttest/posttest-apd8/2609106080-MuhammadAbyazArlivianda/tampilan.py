from prettytable import PrettyTable
from data import koleksi_kartu
from utilitas import hitung_total_rekursif

def cetak_judul(teks):
    print("=" * 40)
    print(teks)
    print("=" * 40)

def tampilkan_koleksi():
    if len(koleksi_kartu) == 0:
        print("Koleksi masih kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama", "Warna", "Angka", "Jumlah"]

        for nomor, kartu in koleksi_kartu.items():
            tabel.add_row([nomor, kartu["nama"], kartu["warna"], kartu["angka"], kartu["jumlah"]])

        tabel.align["Nama"] = "l"
        print(tabel)
        total = hitung_total_rekursif(list(koleksi_kartu.keys()), 0)
        print("Total seluruh kartu:", total)