# TODO 1 Buatlah Fungsi add_expense disini
def add_expense(expenses, date, description, amount):
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    return expenses + [new_expense]

# TODO 2 Buatlah fungsi calculate_total_expenses disini
calculate_total_expenses = lambda expenses, date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)

# TODO 3 Buatlah fungsi get_expenses_by_date disini
get_expenses_by_date = lambda expenses, date: [expense for expense in expenses if expense['tanggal'] == date]

# TODO 4 Buatlah fungsi generate_expenses_report disini
generate_expenses_report = lambda expenses: (f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}" for expense in expenses)

def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    expenses = add_expense(expenses, date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return expenses

def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")

def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
get_user_input = lambda command: int(input(command))

def main():
    expenses = [
        {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
        {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
        {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
    ]

    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            total_expenses = calculate_total_expenses(expenses, date)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == "_main_":
    main()