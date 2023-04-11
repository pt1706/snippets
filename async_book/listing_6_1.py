import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
        if counter in range(0, 1000000000, 5000000):
            print('Обработано: ', counter)
    end = time.time()
    print(f'Закончен подсчет до {count_to} за время {end - start:0.3f} c')
    return counter


if __name__ == "__main__":
    # start_time = time.time()
    # to_one_hundred_million = Process(target=count, args=(50000000,))
    # to_two_hundred_million = Process(target=count, args=(100000000,))
    # to_one_hundred_million.start()
    # to_two_hundred_million.start()
    # to_one_hundred_million.join()
    # to_two_hundred_million.join()

    start_time = time.time()
    to_one_hundred_million = count(50000000)
    to_two_hundred_million = count(100000000)
    end_time = time.time()
    print(f'Полное время работы {end_time-start_time:0.3f} c')