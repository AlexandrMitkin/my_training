import threading
import random
from time import sleep


class Bank:
    def __init__(self, balance1=0):
        self.balance = balance1
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            s1 = random.choice(range(50, 501))
            # random.randint(50,500)
            self.balance += s1
            print(f"Пополнение: {s1}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            s1 = random.choice(range(50, 501))
            # random.randint(50,500)
            print(f"Запрос на {s1}")
            if s1 <= self.balance:
                self.balance -= s1
                print(f"Снятие: {s1}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
