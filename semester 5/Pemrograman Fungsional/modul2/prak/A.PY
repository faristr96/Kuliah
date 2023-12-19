import getpass

# Fungsi untuk login sebagai admin
def admin_login():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")

    if username == "admin" and password == "admin":
        admin()
    else:
        print("Username atau password salah. Silakan coba lagi.")


# Inisialisasi data peserta (kosong)
peserta = []

# Fungsi untuk mengecek hasil akhir
cek_hasil = lambda nilai: "Lolos" if nilai >= 75 else "Tidak Lolos"


# Fungsi untuk admin
def admin():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Peserta")
        print("2. Edit Nilai Peserta")
        print("3. Lihat Data Peserta")
        print("4. Temukan Peserta")
        print("5. Edit Data Peserta")
        print("0. Kembali")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            tambah_peserta()
        elif pilihan == "2":
            edit_nilai_peserta()
        elif pilihan == "3":
            lihat_data()
        elif pilihan == "4":
            temukan_peserta()
        elif pilihan == "5":
            edit_data_peserta()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, 4, 5, 0.")


# Fungsi untuk menambah peserta
def tambah_peserta():
    nama = input("Masukkan nama peserta: ")
    nilai = int(input("Masukkan nilai peserta: "))
    peserta.append({"id": len(peserta), "nama": nama, "nilai": nilai})
    print("Peserta berhasil ditambahkan.")


# Fungsi untuk mengedit nilai peserta
def edit_nilai_peserta():
    id_peserta = int(input("Masukkan ID peserta: "))
    if id_peserta < len(peserta):
        p = peserta[id_peserta]
        print(f"{'ID':<5}{'Nama':<15}{'Nilai':<15}{'Status':<15}")
        print(f"{p['id']:<5}{p['nama']:<15}{p['nilai']:<15}{cek_hasil(p['nilai'])}")
        new_nilai = int(input("Masukkan nilai baru: "))
        peserta[id_peserta]["nilai"] = new_nilai
        print("Nilai berhasil diubah.")
    else:
        print(f"\nID Peserta {id_peserta} tidak ditemukan.")


# Fungsi untuk melihat data peserta
def lihat_data():
    print("\nData Peserta:")
    print(f"{'ID':<5}{'Nama':<15}{'Nilai':<15}{'Status':<15}")  # Header kolom
    [
        print(f"{p['id']:<5}{p['nama']:<15}{p['nilai']:<15}{cek_hasil(p['nilai'])}")
        for p in peserta
    ]


# Fungsi untuk mencari peserta berdasarkan nama
def temukan_peserta():
    nama_peserta = input("\nMasukkan Nama Peserta Anda: ")
    found_peserta = next((p for p in peserta if p["nama"] == nama_peserta), None)
    if found_peserta is not None:
        print(f"{'ID':<5}{'Nama':<15}{'Nilai':<15}{'Status':<15}")
        print(f"{found_peserta['id']:<5}{found_peserta['nama']:<15}{found_peserta['nilai']:<15}{cek_hasil(found_peserta['nilai'])}" )
    else:
        print(f"\nNama Peserta {nama_peserta} tidak ditemukan.")


# Fungsi untuk mengedit data peserta berdasarkan nama
def edit_data_peserta():
    nama_peserta = input("\nMasukkan Nama Peserta yang Ingin Diedit: ")
    found_peserta = next((p for p in peserta if p["nama"] == nama_peserta), None)
    if found_peserta is not None:
        print(f"{'ID':<5}{'Nama':<15}{'Nilai':<15}{'Status':<15}")
        print(
            f"{found_peserta['id']:<5}{found_peserta['nama']:<15}{found_peserta['nilai']:<15}{cek_hasil(found_peserta['nilai'])}"
        )
        new_nama = input("Masukkan nama baru: ")
        found_peserta["nama"] = new_nama
        print("Nama berhasil diubah.")
    else:
        print(f"\nNama Peserta {nama_peserta} tidak ditemukan.")


# Fungsi untuk memilih peran
def menu():
    while True:
        print("\nPilih Peran:")
        print("1. Admin")
        print("2. Peserta")
        print("0. Keluar")
        role = input("Masukkan peran Anda: ")
        if role == "1":
            admin_login()
        elif role == "2":
            print("\nPilihan:")
            print("1. Lihat Info Saya berdasarkan nama")
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                info_peserta()
            else:
                print("Pilihan tidak valid. Silakan masukkan 1")
        elif role == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1")


# Fungsi untuk melihat info peserta berdasarkan nama
def info_peserta():
    nama_peserta = input("\nMasukkan Nama Peserta Anda: ")
    found = False
    for p in peserta:
        if p["nama"] == nama_peserta:
            found = True
            print(f"{'ID':<5}{'Nama':<15}{'Nilai':<15}{'Status':<15}")
            print(f"{p['id']:<5}{p['nama']:<15}{p['nilai']:<15}{cek_hasil(p['nilai'])}")
            break

    if not found:
        print(f"\nNama Peserta {nama_peserta} tidak ditemukan.")


if __name__ == "__main__":
    menu()