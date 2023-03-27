def check_email(email):
    if '@' not in email:
        return False
    lst = email.split('@')
    if '.' not in lst[1]:
        return False
    if '$' in lst[0]:
        return False
    return True


if __name__ == '__main__':
    lst = 'abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com'
    lst = lst.split(' ')
    res = ['abc@it.ru', 'biba123@list.ru', 'sc_lib@list.ru']
    assert res == list(filter(check_email, lst))
