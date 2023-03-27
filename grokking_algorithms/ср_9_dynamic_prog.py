items = {
    "gitar": {'cost': 1500, 'weight': 1},
    "recorder": {'cost': 3000, 'weight': 4},
    "laptop": {'cost': 2000, 'weight': 3},
    "phone": {'cost': 2000, 'weight': 1},
}


def find_optim_dynamic(items, size):
    cell_size = min([v['weight'] for k, v in items.items()])
    max_cost = 0
    lst_items = []
    for item, attr in items.items():
        row_size = 0
        for cell in range(1, int(size / cell_size) + 1):
            row_size += cell
            if attr['weight'] <= row_size and item not in lst_items:
                lst_items += [item]
                max_cost += attr['cost']
    return


find_optim_dynamic(items, 4)
