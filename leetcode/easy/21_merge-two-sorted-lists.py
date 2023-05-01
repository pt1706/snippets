def merge_two_lists(lst_1, lst_2):
    res = []
    while lst_1 and lst_2:
        if lst_1[0] < lst_2[0]:
            item = lst_1[0]
            lst_1 = lst_1[1:]

        else:
            item = lst_2[0]
            lst_2 = lst_2[1:]
        res.append(item)
    res.extend((lst_1 or lst_2))
    return res


if __name__ == '__main__':
    lst_1 = [1, 2, 4]
    lst_2 = [1, 3, 4]
    assert [1, 1, 2, 3, 4, 4] == merge_two_lists(lst_1, lst_2)
    print(merge_two_lists(lst_1, lst_2))