import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

#Ukuran gambar
plt.figure(figsize=(7,5))

#Judul dan label sumbu
plt.title('Percobaan 2')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

#Panjang nilai x dan y
plt.xlim([0, 13])
plt.ylim([0, 13])

#Warna garis
plt.plot(xpoints, ypoints, marker = '*', color = 'blue')
plt.show()