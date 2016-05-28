from .core import Pattern


class CharClass(Pattern):
    char_class = None

    def compile(self):
        return self.char_class


class CharClassMeta(type):
    def __new__(cls, name, parents, dct):
        name = dct['char_class_name']
        return type(name, parents, dct)


def _build_char_class(name, char_cls):
    class C(CharClass, metaclass=CharClassMeta):
        char_class_name = name
        char_class = char_cls

    return C()


CHAR = _build_char_class('Char', '.')
LETTER = _build_char_class('Letter', '[A-Za-z]')
UPPER = _build_char_class('Upper', '[A-Z]')
LOWER = _build_char_class('Lower', '[a-z]')
DIGIT = _build_char_class('Digit', '[0-9]')

