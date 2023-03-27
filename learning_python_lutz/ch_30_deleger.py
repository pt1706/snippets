class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __repr__(self):
        return f'{self.wrapped}'


class Inherited(Wrapper):
    def __getattr__(self, attrname):
        return getattr(self.wrapped, attrname)
