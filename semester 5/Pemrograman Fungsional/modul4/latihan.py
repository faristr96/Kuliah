# Higher-Order Function (HOF)
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Penggunaan HOF
hasil_kali_5 = perkalian(5)
print(hasil_kali_5(3))     #Output: 15

# Currying
def perkalian_currying(a):
    def dengan(b):
        return a * b
    return dengan

# Penggunaan Currying
hasil_kali_3 = perkalian_currying(3)
print(hasil_kali_3(4))  # Output: 12