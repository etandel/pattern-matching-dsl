from .validation import assert_type


class Multiplier(object):
    def compile(self):
        raise NotImplementedError()

    @classmethod
    def create(cls, value):
        assert_type(value, int, tuple, Multiplier)
        factories = {
            int: FixedWidth,
            tuple: Range,
            cls: lambda v: v,
        }
        for multiplier_cls, factory in factories.items():
            if isinstance(value, multiplier_cls):
                return factory(value)


class Whatever(Multiplier):
    def compile(self):
        return '*'


class OneOrMore(Multiplier):
    def compile(self):
        return '+'


WHATEVER = Whatever()
ONE_OR_MORE = OneOrMore()


class Range(Multiplier):
    def __init__(self, range_):
        self.init = assert_type(range_[0], int)
        self.end = assert_type(range_[1], int)

    def compile(self):
        return '{{{},{}}}'.format(self.init, self.end)


class FixedWidth(Multiplier):
    def __init__(self, width):
        self.width = width

    def compile(self):
        return '{{{}}}'.format(self.width)
