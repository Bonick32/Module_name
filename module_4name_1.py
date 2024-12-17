def test_function():
    def inner_function():
        return print('Я в области видимости функции test_function')

    inner_function()

test_function()
# inner_function() # происходит ошибка, так как эта функция вложена в другую функцию
