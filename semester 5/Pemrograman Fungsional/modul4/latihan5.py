def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_m(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def calculate_c(p1, m):
        return p1[1] - m * p1[0]

    M = calculate_m(p1, p2)
    C = calculate_c(p1, M)

    return f"y = {M:.2f}x + {C:.2f}"



print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(4, -2), point(-1, 3)))