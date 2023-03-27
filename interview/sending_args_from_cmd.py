import sys


def get_from_cmd_line(*args):
    print(*args)


if __name__ == '__main__':
    get_from_cmd_line(*[sys.argv[index] for index in range(1, len(sys.argv))])
    print(__name__)