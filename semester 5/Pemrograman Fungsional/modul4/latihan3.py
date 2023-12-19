# Split String Decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string) + " - Then data is splitted")
        return splitted_string
    return wrapper

# Title Decorator
def title_decorator(function):
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " - Data is converted to title case")
        return make_title
    return wrapper

# Penggunaan kedua decorator pada fungsi say_hi
@split_string_decorator
@title_decorator
def say_hi():
    return 'hello there'

# Memanggil fungsi say_hi yang telah di-decorate
result = say_hi()

# Menampilkan hasil
print(result)