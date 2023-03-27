"""
Purpose of snippet to toy with pagination with very simple objects
"""
from django.core.paginator import Paginator

obj = [x for x in 'spamhammam']


def show_content(inp):
    p = Paginator(obj, 2)
    res = p.page(inp)
    return res


if __name__ == '__main__':
    print(show_content(2))
    print(show_content(2).object_list)
    print(show_content(2).has_next())
    print(show_content(2).next_page_number())
    print(show_content(2).has_previous())
