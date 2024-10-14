import multiprocessing
import time
from datetime import datetime


def read_info(name):
    all_data = []
    # path = Path(__file__).parent / 'sekond/file 1.txt'
    with open(name, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


files = ['sekond/file 1.txt', 'sekond/file 2.txt', 'sekond/file 3.txt', 'sekond/file 4.txt']

# filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":

    with multiprocessing.Pool(processes=3) as pool:
        t_start = time.time()
        for i in files:
            read_info(i)
        t_end = time.time()
        print(t_end - t_start)

        # files = ['sekond/file 1.txt', 'sekond/file 2.txt', 'sekond/file 3.txt', 'sekond/file 4.txt']
        t_start = datetime.now()
        pool.map(read_info, files)

        t_end = datetime.now()
        print(t_end - t_start)
