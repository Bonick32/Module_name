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

h1 = House('ЖК Горский', 18)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

# h1.go_to(5)
# h2.go_to('121')

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