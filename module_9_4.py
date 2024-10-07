from random import choice

import random2

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            l = len(data_set)
            k = 0
            for i in data_set:
                k += 1
                file.write(str(i))
                if k < l:
                    file.write("\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words1):
        self.words = words1

    def __call__(self):
        return random2.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
