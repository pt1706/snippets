def simplifyPath(path: str) -> str:
    cur = ''
    stack = []
    for i in path + '/':
        if i == '/':
            if cur == '..':
                if stack:
                    stack.pop()
            elif cur != '' and cur != '.':
                stack.append(cur)
            cur = ''
        else:
            cur += i
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = '/home//foo/'
    # print(simplifyPath(path))
    assert '/home/foo' == simplifyPath(path), 'test 1'

    path = '/home/'
    # print(simplifyPath(path))
    assert '/home' == simplifyPath(path), 'test 2'

    path = '/../'
    # print(simplifyPath(path))
    assert '/' == simplifyPath(path), 'test 3'

    path = '/a/./b/../../c/'
    # print(simplifyPath(path))
    assert '/c' == simplifyPath(path), 'test 4'

    path = '/a/../../b/../c//.//'
    # print(simplifyPath(path))
    assert '/c' == simplifyPath(path), 'test 5'
