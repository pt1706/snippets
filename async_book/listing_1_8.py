import threading
import time
import requests


def read_example() -> None:
    response = requests.get('https://ya.ru')
    print(response.status_code)


first_thread = threading.Thread(target=read_example)
second_thread = threading.Thread(target=read_example)

async_start = time.time()

first_thread.start()
second_thread.start()

print('Все потоки работают!')

first_thread.join()
second_thread.join()
async_end = time.time()
print(f'Синхронное выполнение заняло{async_end - async_start:.4f} с.')