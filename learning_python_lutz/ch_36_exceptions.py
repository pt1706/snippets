import sys


def safe(func, *fargs, **fkwargs):
    if 'counter' not in fkwargs.keys():
        fkwargs['counter'] = 0

    def wrapper(*args, **kwargs):
        fkwargs['counter'] += 1
        try:
            return func(*args, **kwargs)
        except Exception:
            fkwargs['exception'] = sys.exc_info()[2]
            return fkwargs
    return wrapper


class MyError(Exception):
    ...


def oops():
    raise MyError('test')
    return None


if __name__ == '__main__':
    t = safe(oops)
    print(t()['exception'])
