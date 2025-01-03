class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value     # изначально записал для __add__ и __radd__ так:
        return self                        # self.number_of_floors = self.number_of_floors + value
                                           # но потом проверил, что работает и так тоже, по крайней мере для этой ситуации
    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__





# h1 = House('ЖК Горский', 18)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(len(h1))
# print(len(h2))
# h1.go_to(5)
# h2.go_to('121')
#
# class House2:
#     def __init__(self, name, number_of_floors):
#         self.name = name
#         self.number_of_floors = int(number_of_floors)
#
#     def go_to2(self, new_floor):
#         new_floor = int(new_floor)
#
#         print(f'поднимаемся на этаж №{new_floor}:')
#         if new_floor > self.number_of_floors or new_floor < 1:
#             print('Такого этажа не существует')
#         else:
#             for i in range(new_floor):
#                 print(i+1)
#     def __str__(self):
#         return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
#
#     def __len__(self):
#         return self.number_of_floors
#
# h3 = House2('Sweet Home', 2)
# print(h3)
# h3.go_to2(3)