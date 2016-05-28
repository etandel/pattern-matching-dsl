from pattern import Literal, WHATEVER, ONE_OR_MORE

from .base import PatternTestCase


class TestCore(PatternTestCase):
    def test_literal_value(self):
        self.assert_matches(Literal('hello'), 'hello')

    def test_concat(self):
        p1 = Literal('hel') + Literal('lo')
        p2 = Literal('hel') + 'lo'
        self.assert_matches(p1, 'hello')
        self.assert_matches(p2, 'hello')

        self.assert_doesnt_match(p1, 'hel')
        self.assert_doesnt_match(p1, 'lo')
        self.assert_doesnt_match(p2, 'hel')
        self.assert_doesnt_match(p2, 'lo')

    def test_alternate(self):
        p1 = Literal('hi') | Literal('hello')
        p2 = Literal('hi') | 'hello'

        self.assert_matches(p1, 'hi')
        self.assert_matches(p2, 'hi')

        self.assert_matches(p1, 'hello')
        self.assert_matches(p2, 'hello')

    def test_multiply__int(self):
        p = Literal('a') * 3
        self.assert_matches(p, 'aaa' * 3)
        self.assert_matches(p, 'aaaa' * 4)

        self.assert_doesnt_match(p, 'a' * 0)
        self.assert_doesnt_match(p, 'a' * 1)
        self.assert_doesnt_match(p, 'a' * 2)

    def test_multiply__tuple(self):
        p = Literal('a') * (3, 5)

        self.assert_matches(p, 'a' * 3)
        self.assert_matches(p, 'a' * 4)
        self.assert_matches(p, 'a' * 5)

        self.assert_doesnt_match(p, 'a' * 0)
        self.assert_doesnt_match(p, 'a' * 1)
        self.assert_doesnt_match(p, 'a' * 2)

    def test_multiply__whatever(self):
        p = Literal('a') * WHATEVER

        self.assert_matches(p, 'a' * 0)
        self.assert_matches(p, 'a' * 1)
        self.assert_matches(p, 'a' * 3)
        self.assert_matches(p, 'a' * 100)

    def test_multiply__one_or_more(self):
        p = Literal('a') * ONE_OR_MORE

        self.assert_matches(p, 'a' * 1)
        self.assert_matches(p, 'a' * 3)
        self.assert_matches(p, 'a' * 100)

        self.assert_doesnt_match(p, 'a' * 0)

    def test_complex_expressions_are_properly_grouped(self):
        p = (Literal('a') * 3 | Literal('b')) * 2 | Literal('c') * 4

        self.assert_matches(p, 'aaaaaa')
        self.assert_matches(p, 'bb')
        self.assert_matches(p, 'cccc')

        self.assert_doesnt_match(p, '')
        self.assert_doesnt_match(p, 'aaa')
        self.assert_doesnt_match(p, 'b')
        self.assert_doesnt_match(p, 'ccc')

