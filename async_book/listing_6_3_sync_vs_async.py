import time
from multiprocessing import Pool


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
        if counter in range(0, 1000000000, 500000):
            print('Обработано: ', counter)
    end = time.time()
    print(f'Закончен подсчет до {count_to} за время {end - start:0.3f} c')
    return counter


if __name__ == "__main__":
    with Pool() as process_pool:  # A
        start_time = time.time()
        to_one_hundred_million = process_pool.apply(count, args=(5000000,))
        to_two_hundred_million = process_pool.apply(count, args=(10000000,))
        end = time.time()
        print(f'all time: {end - start_time:0.3f} c')

    # with Pool() as process_pool:  # A
    #     start_time = time.time()
    #     to_one_hundred_million = process_pool.apply_async(count, args=(5000000,))
    #     to_two_hundred_million = process_pool.apply_async(count, args=(10000000,))
    #     print(to_one_hundred_million.get())
    #     print(to_two_hundred_million.get())
    #     end = time.time()
    #     print(f'all time: {end - start_time:0.3f} c')