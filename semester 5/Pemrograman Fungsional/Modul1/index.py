
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")
        if username == self.username and password == self.password:
            print("\nLogin sukses sebagai admin.")
            self.menu_admin()
        else:
            print("\nLogin gagal. Coba lagi.")


    def tambah_peserta(self):
        nama = input("Masukkan nama peserta: ")
        while True:
            nilai_input = input("Masukkan nilai peserta: ")
            if nilai_input.isdigit():
                nilai = float(nilai_input)
                hasil_akhir = "Lulus" if nilai >= 75 else "Tidak Lulus"

                data_peserta = {'ID': len(peserta), 'Nama': nama, 'Nilai': nilai, 'Hasil Akhir': hasil_akhir}
                peserta.append(data_peserta)
                print("\nPeserta berhasil ditambahkan.")
                break
            else:
                print("\nInput nilai tidak valid. Harap masukkan angka.")

    def lihat_daftar_peserta(self):
        print("\nDaftar Peserta:")
        if not peserta:
            print("Belum ada peserta terdaftar.")
        else:
            print(f"{'ID':<5}{'Nama':<20}{'Nilai':<10}{'Hasil Akhir':<15}")
            print("-" * 50)
            for data in peserta:
                print(f"{data['ID']:<5}{data['Nama']:<20}{data['Nilai']:<10}{data['Hasil Akhir']:<15}")

    def edit_nilai_peserta(self):
        id = int(input("Masukkan ID peserta yang akan diedit nilainya: "))
        data = next((p for p in peserta if p['ID'] == id), None)
        if data:
            new_nilai = float(input("Masukkan nilai baru peserta: "))
            data['Nilai'] = new_nilai
            data['Hasil Akhir'] = "Lulus" if new_nilai >= 75 else "Tidak Lulus"
            print("Nilai peserta berhasil diubah.")
        else:
            print("\nPeserta tidak ditemukan. Silakan coba lagi.")

    def menu_admin(self):
        while True:
            print("\nMenu Admin:")
            print("1. Tambahkan peserta")
            print("2. Lihat daftar peserta")
            print("3. Edit nilai peserta")
            print("4. Keluar")

            pilihan = input("Pilih : ")

            if pilihan == '1':
                self.tambah_peserta()
            elif pilihan == '2':
                self.lihat_daftar_peserta()
            elif pilihan == '3':
                self.edit_nilai_peserta()
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")



class Peserta:
    def __init__(self, ID, nama, nilai):
        self.ID = ID
        self.nama = nama
        self.nilai = nilai
        self.hasil_akhir = "Lulus" if nilai >= 75 else "Tidak Lulus"

    def lihat_nilai_dan_hasil_akhir(self):
        print(f"{'ID':<5}{'Nama':<20}{'Nilai':<10}{'Hasil Akhir':<15}")
        print("-" * 50)
        print(f"{self.ID:<5}{self.nama:<20}{self.nilai:<10}{self.hasil_akhir:<15}")
        # print(f"ID: {self.ID}")
        # print(f"Nilai Anda: {self.nama}")
        # print(f"Nilai Anda: {self.nilai}")
        # print(f"Hasil Akhir Anda: {self.hasil_akhir}")

    def menu_peserta(self):
        while True:
            print("\nMenu Peserta:")
            print("1. Lihat nilai dan hasil akhir")
            print("2. Keluar")

            pilihan = input("Pilih : ")

            if pilihan == '1':
                self.lihat_nilai_dan_hasil_akhir()
            elif pilihan == '2':
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

# akun
akun_admin = Admin('admin', 'admin123')
peserta = []

# Main program
while True:
    print("\nSelamat datang!")
    print("1. Masuk sebagai admin")
    print("2. Masuk sebagai peserta")

    pilihan = input("Pilih: ")

    if pilihan == '1':
        akun_admin.login()
    elif pilihan == '2':
        id = int(input("Masukkan ID peserta: "))
        data = next((p for p in peserta if p['ID'] == id), None)
        if data:
            peserta_menu = Peserta(data['ID'], data['Nama'], data['Nilai'])
            peserta_menu.menu_peserta()
        else:
            print("Peserta tidak ditemukan. Silakan coba lagi.")
    else:
        print("Pilihan tidak valid. Coba lagi.")