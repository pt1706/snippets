class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False

    def __repr__(self):
        res = 'children:'
        for k in self.children:
            res += f' {k}'
        res += f'end of word: {self.end_word}.'
        return res


class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_word = True

    def search(self, word: str) -> bool:
        cur = self.node
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    assert True is t.search('apple')
    assert False is t.search('app')
    assert True is t.startsWith('app')
    t.insert('app')
    assert True is t.search('app')

    t = Trie()
    t.insert('app')
    t.insert('apple')
    t.insert('beer')
    t.insert('add')
    t.insert('jam')
    t.insert('rental')
    assert False is t.search('apps')
    assert True is t.search('app')
    assert False is t.search('ad')
