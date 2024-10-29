from threading import Thread
import random
import queue
from time import sleep
import threading


class Table:
    def __init__(self, number1, guest1=None):
        self.number = number1
        self.guest = guest1

class Guest(threading.Thread):
    def __init__(self, name1):
        threading.Thread.__init__(self)
        self.name = name1

    def run(self):
        #print(f"гость {self.name} спит ")
        sleep(random.randint(3, 10))
        #print(f"гость {self.name} проснулся ")

class Cafe:
    def __init__(self, *tables1):
        self.tables = tables1
        self.queue=queue.Queue()

    def guest_arrival(self, *guests):
        l = len(guests)
        i1=0
        for i in self.tables:
            if i.guest == None and i1 < l:
                g2 = guests[i1].name
                i.guest = g2
                print(f"{g2} сел(-а) за стол номер {i.number}")
                guests[i1].start()
            i1 +=1
        #если гости усажены не все, то добавляем в очередь
        if i1<l:
            for j in range(i1, l):
                g2 = guests[j]
                print(f"{g2.name} в очереди")
                self.queue.put(g2)

    def discuss_guests(self):
        #определяем, что не все столы свободны
        r = 0
        for i in self.tables:
            if i.guest != None:
                r = 1
                break
        #если очередь не пуста или есть занятые столы, то обслуживаем
        while self.queue.empty() == False or r == 1:
            r1=0
            k1=0
            #ищем стол, где гость покушал
            #r1 - флаг того, все столы заняты
            #пока столы заняты, ждём и смотрим за гостями за столами
            while r1==0:
                for i in self.tables:
                    #определяем имя гостя за столом
                    if i.guest != None:
                        #определяем поток гостя по его имени
                        for j in guests:
                            if j.name == i.guest:
                                #смотрим, покушал ли гость?
                                if j.is_alive() == False:
                                    print(f"{i.guest} покушал(-а) и ушёл(ушла)")
                                    print(f"Стол номер {i.number} свободен")
                                    i.guest = None
                                    #запоминаем номер стола и запоминаем, что освободили
                                    k1=i.number-1
                                    r1=1
                                    r=0
                                break
            #стол освободился. Если очередь не пуста, то сажаем за стол следующего
            if self.queue.empty() == False:
                g2 = self.queue.get()
                # print("k1= ", k1)
                # print("g2.name= ", g2.name)
                tables[k1].guest = g2.name
                print(f"{g2.name} вышел(-ла) из очереди и сел(-а) за стол номер {k1+1}")
                #запоминаем, что не все столы пусты
                r=1
                g2.start()





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

