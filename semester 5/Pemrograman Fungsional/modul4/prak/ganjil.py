import numpy as np
import matplotlib.pyplot as plt

def transform_point(point, translation, rotation_angle, scale):
    # Translasi
    translated_point = np.array(point) + np.array(translation)

    # Rotasi sejajar sumbu x positif
    rotation_matrix = np.array([[np.cos(np.radians(rotation_angle)), -np.sin(np.radians(rotation_angle))],
                                [np.sin(np.radians(rotation_angle)), np.cos(np.radians(rotation_angle))]])
    rotated_point = np.dot(rotation_matrix, translated_point)

    # Perbesaran skala
    scaled_point = rotated_point * np.array(scale)

    return scaled_point

def calculate_line_equation(point, gradient):
    # Menghitung persamaan garis
    b = point[1] - gradient * point[0]
    return gradient, b

def plot_transformed_line(point, gradient, translation, rotation_angle, scale):
    # Menghitung persamaan garis awal
    m_original, b_original = calculate_line_equation(point, gradient)

    print(f"Persamaan garis yang melalui titik ({point[0]},{point[1]}) dan bergradien {gradient:.2f}:")
    print(f"y = {gradient:.2f}x + {b_original:.2f}")

    # Transformasi titik A
    transformed_point_A = transform_point(point, translation, rotation_angle, scale)

    # Menghitung persamaan garis setelah transformasi
    m_transformed, b_transformed = calculate_line_equation(transformed_point_A, gradient)

    print("Persamaan garis baru setelah transformasi:")
    print(f"y = {m_transformed:.2f}x + {b_transformed:.2f}")


# Input pilihan menggunakan NIM atau nilai tetap
choice = int(input("Pilih (1 untuk NIM, 2 untuk nilai tetap): "))

# Implementasi switch case menggunakan if-elif-else
if choice == 1:
    nim = int(input("Input NIM : "))

    x = nim // 100
    y = (nim % 100) // 10 
    z = nim % 10

    point_A = [x, y]
    point_B = [y, z]
    gradient = x

    translation = [y, z]
    rotation_angle = 60
    scale = [z, x]

    plot_transformed_line(point_A, gradient, translation, rotation_angle, scale)

elif choice == 2:
    point_A = [3, 4]
    gradient = 2

    translation = [2, -3]
    rotation_angle = 60
    scale = [1.5, 2]

    plot_transformed_line(point_A, gradient, translation, rotation_angle, scale)

else:
    print("Pilihan tidak valid.")