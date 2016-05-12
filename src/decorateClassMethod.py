def decorator(args):
    def _deco(func):
        def _func(self):
            self.i = args
            func(self)
        return _func

    return _deco


class Foo(object):
    i = 1

    @decorator(234)
    def bar(self):
        print('i:', self.i)


f = Foo()
f.bar()
