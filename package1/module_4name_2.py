# # sortfunc
#
# nums = [5, 6, 3, 2, 1, 4]
#
# def buble_sort(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) - 1):
#             if ls[i] > ls[i+1]:
#                 ls[i], ls[i+1] = ls[i+1], ls[i]
#                 swapped = True
#
# # buble_sort(nums)
# # print(nums)
#
# def selection_sort(ls):
#     for i in range(len(ls)):
#         lowest = i
#         for j in range(i + 1, len(ls)):
#             if ls[j] < ls[lowest]:
#                 lowest = j
#         ls[i], ls[lowest] = ls[lowest], ls[i]
#
# # print(nums)
# # selection_sort(nums)
# # print(nums)
#



import names
from time import time

def decor(func,*args):
    ls = args[0]
    print('получил', ls)
    start = time()
    func(*args)
    stop = time()
    print('отдал', ls)
    print('время', stop-start)

#0.2
def bubble_sort(ls, reverse = False):
    compare = (lambda x,y : x > y) if not reverse else (lambda x,y : x < y)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls)-1):
            if compare(ls[i], ls[i+1]):
                ls[i], ls[i + 1] = ls[i+1], ls[i]
                swapped = True


# 0.03
def selection_sort(ls):
    for i in range(len(ls)): # i - кол уже проверенных
        low = i
        for j in range(i+1,len(ls)):
            if ls[low] > ls[j]:
                low = j
        ls[low],ls[i] = ls[i],ls[low]

def insertion_sort(ls):
    for i in range(1, len(ls)):
        item = ls[i]
        j = i - 1
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = item

# 0.001
def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    el = ls[len(ls)//2]
    l = [i for i in ls if i< el]
    m = [i for i in ls if i == el]
    r = [i for i in ls if i > el]


    return quick_sort(l) + m +  quick_sort(r)

def sort_(ls):
    ls = sorted(ls)
    return print(ls)




ls = [names.get_first_name() for i in range(10000)]

# def ls_(name): #проверил скорость создания списка имен
#     start = time()
#     name =  [names.get_first_name() for i in range(10000)]
#     stop = time()
#     print('отдал', name)
#     print('время', stop - start)
#
# name = []
# ls_(name)

decor(sort_, ls)


# print(ls)
# ls = quick_sort(ls)
# print(ls)
