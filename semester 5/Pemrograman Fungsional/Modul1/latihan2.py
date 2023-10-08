# [] random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Inisialisasi str_list (untuk string), float_tuple (untuk float), dan int_dict (untuk int)
str_list = []
float_tuple = ()
int_dict = {}

# Loop melalui setiap elemen dalam random_list
for item in random_list:
    if isinstance(item, int):
        # Pisahkan angka satuan, puluhan, dan ratusan untuk integer
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100
        int_dict[item] = {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}
    elif isinstance(item, float):
        # Gabungkan data float ke dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Gabungkan data string ke dalam list
        str_list.append(item)

# Hasilnya
print("List of Strings:", str_list)
print("Tuple of Floats:", float_tuple)
print("Dictionary of Integers:", int_dict)