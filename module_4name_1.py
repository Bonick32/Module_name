from random import randint
# def test_function():
#     def inner_function():
#         return print('Я в области видимости функции test_function')
#
#     inner_function()
#
# test_function()
# # inner_function() # происходит ошибка, так как эта функция вложена в другую функцию


MAX_BUNCHES = 5
MAX_BUNCHE_SIZE = 20

_holder = {}
_sorted_keys = None

def put_stones():
    """ расположить камни на игровой поверхности """
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHE_SIZE)
    _sorted_keys = sorted(_holder.keys())