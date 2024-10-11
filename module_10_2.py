from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name1, power1):
        super().__init__()
        self.name = name1
        self.power = power1
        self.number_warriors = 100
        print(f"{self.name}, на нас напали!")
        self.t_start = time.time()

    def run(self):
        n = 0
        while self.number_warriors > 0:
            n += 1
            time.sleep(1)
            self.number_warriors -= self.power
            print(f"{self.name} сражается {n} дней, осталось {self.number_warriors} воинов.\n")
        t_end = time.time()
        print(f"{self.name} одержал победу спустя {round(t_end - self.t_start, 2)} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончились!")
