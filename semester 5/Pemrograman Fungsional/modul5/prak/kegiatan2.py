import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Mengekstrak harga produk dan jumlah terjual/TODO 1
harga_produk = [item[1] for item in data_transaksi]
jumlah_terjual = [item[2] for item in data_transaksi]

print("Harga Produk:", harga_produk)
print("Jumlah Produk Terjual:", jumlah_terjual)

# ScatterPlot/TODO 2
plt.scatter(harga_produk, jumlah_terjual)
plt.title("Hubungan Harga Produk dan Jumlah Produk Terjual")
plt.xlabel("Harga Produk")
plt.ylabel("Jumalah Produk Terjual")
plt.show()

# Hitung total pendapatan untuk setiap produk/TODO 3
total_pendapatan = list(
    map(lambda harga, terjual: harga * terjual, harga_produk, jumlah_terjual)
)

print("Total Pendapatan untuk Setiap Produk:", total_pendapatan)

# BarChart/TODO 4
nama_produk = [item[0] for item in data_transaksi]

plt.bar(nama_produk, total_pendapatan, color="red")
plt.title("Pendapatan Produk")
plt.xlabel("Nama Produk")
plt.ylabel("Pendapatan Produk")
plt.show()