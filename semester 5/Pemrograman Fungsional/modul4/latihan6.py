# Untuk NIM ganjil
def point(x, y):
    return x, y

def line_equation_of(p1, M):
    def calculate_C(p1, M):
        x1, y1 = p1
        return y1 - M * x1

    C = calculate_C(p1, M)
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (3, 0) dan bergradien 5:")
print(line_equation_of(point(3, 0), 5))  # Ubah nilai input dengan 3 digit nim akhir kalian

