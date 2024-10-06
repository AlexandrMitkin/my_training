# def greet_person(person_name):
#     if person_name == "ВаленДеМорт":
#         raise Exception("Мы не любим тебя, ВаленДеМорт")
#     print(f"Привет, {person_name}")
#
#
# greet_person("Дорогой ученик")
# greet_person("ВаленДеМорт")
from pyexpat.errors import messages


class IncorrectVinNumber(Exception):
    def __init__(self, message1):
        self.message = message1


class IncorrectCarNumbers(Exception):
    def __init__(self, message1):
        self.message = message1


class fff:
    def __init__(self, ggg):
        self.ggg = ggg


class Car:
    def __init__(self, model1, vin1, numbers1):
        self.model = model1
        # self.vin=vin1
        # self.numbers=numbers1
        try:
            Car.is_valid_vin(vin1)
            self.__vin = vin1
        except IncorrectVinNumber as e:
            print(e.message, end=' ')
            raise IncorrectVinNumber("")
        try:
            Car.__is_valid_numbers(numbers1)
            self.__numbers = numbers1
        except IncorrectCarNumbers as e:
            print(e.message, end=' ')
            raise IncorrectCarNumbers("")

    def is_valid_vin(vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if vin_number < 1_000_000 or vin_number > 9_999_999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")

        return True

    def __is_valid_numbers(numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")

        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
