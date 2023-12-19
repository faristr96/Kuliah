from functools import reduce
import matplotlib.pyplot as plt

# List nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata nilai
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# Membuat label mahasiswa dan nilai secara fungsional
data_mahasiswa = list(map(lambda index: (f"Mahasiswa {index} = {nilai_mahasiswa[index - 1]}"), range(1, len(nilai_mahasiswa) + 1)))
print(data_mahasiswa)

# Membuat diagram batang dengan label dan nilai sesuai index
plt.bar(range(1, len(nilai_mahasiswa) + 1), nilai_mahasiswa, color='blue')
plt.axhline(rata_rata, color='red', linestyle='dashed', label=f'Rata-rata = {rata_rata:.2f}')
plt.xlabel("Mahasiswa")
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.legend()
plt.show()