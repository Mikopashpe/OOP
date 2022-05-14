'''

'''


class Attrdisplay:
    def gatherattrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s:%s]' % (self.__class__.__name__, self.gatherattrs())


if __name__ == '__main__':
    class Toptest(Attrdisplay):
        count = 0
        def __init__(self):
            self.attr1 = Toptest.count
            self.attr2 = Toptest.count+1
            Toptest.count+2
     
    class Subtest(Toptest):
        pass


x, y = Toptest(), Subtest()
print(x)
print(y)