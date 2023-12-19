def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

# Memanggil fungsi say_hi yang telah di-decorate
result = say_hi()

# Menampilkan hasil
print(result)