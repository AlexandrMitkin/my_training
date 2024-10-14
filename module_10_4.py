from threading import Thread
import random
import queue
from time import sleep


class Table:
    def __init__(self, number1, guest1=None):
        self.number = number1
        self.guest = guest1


class Guest(Thread):
    q = queue.Queue()

    def __init__(self, name1):
        super().__init__()
        self.name = name1

    def run(self):
        sleep(random.randint(3, 10))


class Cafe(Guest):
    i1 = 0

    def __init__(self, *tables1):
        Guest.__init__(self, name1="")
        self.tables = tables1

    def guest_arrival(self, *guests):
        l = len(guests)
        for i in self.tables:
            if i.guest == None and Cafe.i1 < l:
                g2 = guests[Cafe.i1].name
                i.guest = g2
                print(f"{g2} сел(-а) за стол номер {i.number}")
                guests[Cafe.i1].start()
                Cafe.i1 += 1
        if Cafe.i1 < l:
            for j in range(Cafe.i1, l):
                g2 = guests[j].name
                print(f"{g2} в очереди")
                Guest.q.put(g2)
        for j in range(Cafe.i1):
            guests[j].join()

    def discuss_guests(self):
        r = 0
        for i in self.tables:
            if i.guest != None:
                r = 1
                break

        if Guest.q.empty() == False or r == 1:
            for i in self.tables:
                if i.guest != None:
                    k = 0
                    for j in guests:
                        if j.name == i.guest:
                            break
                        k += 1
                    # k - номер в guest, который сидит за столом
                    # проверяем, поел или нет
                    # если нет, то переход к следующему столу i
                    if guests[k].is_alive() == False:
                        print(f"{i.guest} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {i.number} свободен")
                        i.guest = None
                        if Guest.q.empty() == False:
                            g2 = Guest.q.get()
                            print(f"{g2} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}")
                            k = 0
                            for j in guests:
                                if j.name == g2:
                                    break
                                k += 1
                            # k - номер гостя, который сел за стол
                            guests[k].start()
                            guests[k].join()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
