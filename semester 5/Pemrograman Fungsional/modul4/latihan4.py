import math

# Fungsi translasi
def translasi(tx, ty):
    def inner_translasi(x, y):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return inner_translasi

# Fungsi dilatasi
def dilatasi(sx, sy):
    def inner_dilatasi(x, y):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return inner_dilatasi

# Fungsi rotasi
def rotasi(sudut):
    def inner_rotasi(x, y):
        sudut_radian = math.radians(sudut)
        new_x = x * math.cos(sudut_radian) - y * math.sin(sudut_radian)
        new_y = x * math.sin(sudut_radian) + y * math.cos(sudut_radian)
        return new_x, new_y
    return inner_rotasi

# Titik awal
titik_p = (3, 5)

# Translasi
translasi_func = translasi(2, -1)
koordinat_translasi = translasi_func(*titik_p)
print(f"Koordinat setelah translasi: {koordinat_translasi}")

# Dilatasi
dilatasi_func = dilatasi(2, -1)
koordinat_dilatasi = dilatasi_func(*titik_p)
print(f"Koordinat setelah dilatasi: {koordinat_dilatasi}")

# Rotasi
rotasi_func = rotasi(30)
koordinat_rotasi = rotasi_func(*titik_p)
print(f"Koordinat setelah rotasi: {koordinat_rotasi}")