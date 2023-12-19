import math

def translasi(tx, ty):
    def inner_translasi(x, y):
        new_x = x + tx

        return new_x
    return inner_translasi


def rotasi(sudut):
    def inner_rotasi(x, y):
        sudut_radian = math.radians(sudut)
        new_x = x * math.cos(sudut_radian) - y * math.sin(sudut_radian)
        new_y = x * math.sin(sudut_radian) + y * math.cos(sudut_radian)
        return new_x, new_y
    return inner_rotasi


def dilatasi(sx, sy):
    def inner_dilatasi(x, y):
        new_x = x * sx

        return new_x
    return inner_dilatasi


def line_equation_of(x, y, M):

    C = y - M * x


    return f"y = {M:.2f}x + {C:.2f}"


input_x = float(input("Masukkan nilai x untuk titik_A: "))
input_y = float(input("Masukkan nilai y untuk titik_A: "))
titik_A = (input_x, input_y)

M_awal = float(input("Masukkan nilai gradien (M_awal): "))


print(f"Persamaan garis yang melalui titik {titik_A} dan bergradien {M_awal}:")
persamaan_garis_awal = line_equation_of(*titik_A, M_awal)
print(persamaan_garis_awal)

# Transformasi beruntun
translasi_func = translasi(0, 5)
rotasi_func = rotasi(60)
dilatasi_func = dilatasi(1, 3)
# tx = 2 ty= -3
# 60
# 1.5 2


titik_transformasi = dilatasi_func(*rotasi_func(*translasi_func(*titik_A)))


M_transformasi = 2


print("Persamaan garis baru setelah transformasi:")
persamaan_garis_transformasi = line_equation_of(*titik_transformasi, M_transformasi)
print(persamaan_garis_transformasi)