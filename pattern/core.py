import re

from .multiplier import Multiplier
from .validation import assert_type


def _protect(value):
    return '(?:{})'.format(value)


def _to_pattern(value):
    return value if isinstance(value, Pattern) else Literal(value)


class Pattern(object):
    def compile(self):
        raise NotImplementedError()

    def match(self, string):
        m = re.match(self.compile(), string)
        return m.string if m else None

    def __add__(self, other):
        return Concat(self, other)

    def __or__(self, other):
        return Alternation(self, other)

    def __mul__(self, other):
        return Repetition(self, other)


class Literal(Pattern):
    def __init__(self, literal):
        assert_type(literal, str)
        self.value = literal

    def compile(self):
        return _protect(self.value)


class Concat(Pattern):
    def __init__(self, pattern1, pattern2):
        self.pattern1 = _to_pattern(pattern1)
        self.pattern2 = _to_pattern(pattern2)

    def compile(self):
        return _protect(self.pattern1.compile() + self.pattern2.compile())


class Alternation(Pattern):
    def __init__(self, pattern1, pattern2):
        self.pattern1 = _to_pattern(pattern1)
        self.pattern2 = _to_pattern(pattern2)

    def compile(self):
        return _protect('{}|{}'.format(self.pattern1.compile(),
                                       self.pattern2.compile()))


class Repetition(Pattern):
    def __init__(self, pattern, multiplier):
        self.pattern = _to_pattern(pattern)
        self.multiplier = Multiplier.create(multiplier)

    def compile(self):
        return _protect(self.pattern.compile() + self.multiplier.compile())

