import os
import inquirer
from data import koleksi_kartu, daftar_warna

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tekan_enter(pesan="Tekan Enter untuk lanjut..."):
    input(pesan)

def pilih_menu(pesan, daftar_pilihan):
    pertanyaan = [
        inquirer.List(
            "menu",
            message=pesan,
            choices=daftar_pilihan,
        ),
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]

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