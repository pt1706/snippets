from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    shared_int.value = shared_int.value + 1


def increment_value_with_lock(shared_int: Value):
    shared_int.get_lock().acquire()
    shared_int.value = shared_int.value + 1
    shared_int.get_lock().release()


def test(target):
    integer = Value('i', 0)
    expected = 0
    for _ in range(100):
        procs = [
            Process(target=target, args=(integer,)),
            Process(target=target, args=(integer,))
        ]
        expected += 2
        [p.start() for p in procs]
        [p.join() for p in procs]
        print(f'Expected: {expected}, actual: {integer.value}')


if __name__ == '__main__':
    test(increment_value)
    test(increment_value_with_lock)


