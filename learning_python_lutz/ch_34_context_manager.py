def find_lines_len_more_6(file_name: str) -> int:
    counter = 0
    with open(file_name, 'r') as file:
        for string in file:
            if len(string.rstrip()) > 6:
                counter += 1
            continue
    return counter


if __name__ == "__main__":
    assert find_lines_len_more_6('test.txt') == 0
    assert find_lines_len_more_6('test1.txt') == 1
    assert find_lines_len_more_6('test2.txt') == 3
    assert find_lines_len_more_6('test3.txt') == 4
    print("all tets passed")


# ------------------2 exercice-----------------------------------


def unique_word_counter(file_name: str) -> int:
    lst = []
    with open(file_name, 'r') as f:
        for i in f:
            i = list(map(lambda x: x.rstrip('\n').lower(), i.split(' ')))
            lst += i
    return len(set(lst))


if __name__ == "__main__":
    assert unique_word_counter('lorem.txt') == 143
    print("all tets passed")


# ------------------3 exercice-----------------------------------


class MyContexManager:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


# ------------------4 exercice-----------------------------------


with MyContexManager('test.txt', 'w') as opened_file:
    opened_file.append('s')


class CustomManager():
    def __init__(self, file_name, method):
        print('init instance')
        self.file_name = open(file_name, method)

    def __enter__(self):
        print(f'entre in file: {self.file_name}')
        return self.file_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'exit from file: {self.file_name}')
        print(exc_type, exc_val)
        return self.file_name.close()


with CustomManager('text.txt', 'w') as f:
    f.write("Hello World")
    raise Exception("Artificial exception")
