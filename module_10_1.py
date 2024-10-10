import time
from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i + 1} \n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
time_start1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_end1 = time.time()
time_res = time_end - time_start
time_res1 = time_end1 - time_start1
print(time_res, " ", time_res1)

time_start = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'example1.txt'))
thr_second = Thread(target=write_words, args=(30, 'example1.txt'))
thr_third = Thread(target=write_words, args=(200, 'example1.txt'))
thr_four = Thread(target=write_words, args=(100, 'example1.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()
time_end = datetime.now()

time_res = time_end - time_start
print(time_res)
