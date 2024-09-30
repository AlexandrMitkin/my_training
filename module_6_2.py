class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner1, model1, engine_power1, color1):
        self.owner = owner1
        self.__model = "model_a1"
        self.__engine_power = "power_b1"
        self.__color = "blue"

    def get_model(self):
        return f"Модель: {self._model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power}"

    def get_color(self):
        return f"Цвет: {self._color}"

    def print_info(self):
        print("\033[34m" + self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        r = 0
        for i in self.__COLOR_VARIANTS:
            if i.upper() == new_color.upper():
                r = 1
                self._color = "\033[32m" + new_color + "\033[34m"
        if r == 0:
            self.owner = "\033[32m" + self.owner
            print(f"\033[31mНельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner1, model1, color1, engine_power1):
        self.owner = owner1
        self._model = model1
        self._engine_power = engine_power1
        self._color = color1


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
