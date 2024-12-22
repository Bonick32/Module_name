class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors) # в тексте задания обратил внимание на уточнение "номер этажа(int)"
                                                      # понимая, что здесь при практике будет значение, введенное пользователем через
                                                      # input, что является строкой, необходимо перевести ее в число
    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

# ниже немного расширил код для дз, как мне кажется более информативный при выводе в консоль)

class House2:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to2(self, new_floor):
        new_floor = int(new_floor)
        print(f'всего этажей в "{self.name}" - {self.number_of_floors}')
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'поднимаемся на этаж №{new_floor}:')
            print('Такого этажа не существует')
        else:
            print(f'поднимаемся на этаж №{new_floor}:')
            for i in range(new_floor):
                print(i+1)

h1 = House('ЖК Горский', '18')
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to('10')

h3 = House2(input('Введите название здания: '), input('количество этажей: '))
h3.go_to2(input('на какой этаж подняться: '))