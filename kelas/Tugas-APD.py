mahasiswa = {
    "nama": "Abyaz",
    "NIM": "230001",
    "prodi": "Informatika",
    "semester": 3
}

mahasiswa.update({
    "alamat": "Samarinda",
    "email": "Abyaz@Gmail.com"
})

mahasiswa["semester"] = 4

print("Jumlah item:", len(mahasiswa))

print("\nData Mahasiswa:")
for key, val in mahasiswa.items():
    print(key, ":", val)

mahasiswa.pop("alamat")

print("\nData Setelah Alamat Dihapus:")
for key, val in mahasiswa.items():
    print(key, ":", val)