import unittest
from pattern.multiplier import Multiplier, FixedWidth, Range
from pattern.multiplier import WHATEVER, ONE_OR_MORE


class TestMultipler(unittest.TestCase):
    def test__create__fixed_width(self):
        self.assertIsInstance(Multiplier.create(23), FixedWidth)

    def test__create__range(self):
        self.assertIsInstance(Multiplier.create((23, 27)), Range)

    def test__create__multiplier(self):
        self.assertEqual(Multiplier.create(WHATEVER), WHATEVER)
        self.assertEqual(Multiplier.create(ONE_OR_MORE), ONE_OR_MORE)

    def test__create__bad_argument(self):
        self.assertRaises(ValueError, Multiplier.create, '1234')


class TestWhatever(unittest.TestCase):
    def test_compile(self):
        self.assertEqual(WHATEVER.compile(), '*')


class TestOneOrMore(unittest.TestCase):
    def test_compile(self):
        self.assertEqual(ONE_OR_MORE.compile(), '+')


class TestFixedWidth(unittest.TestCase):
    def test_compile(self):
        self.assertEqual(FixedWidth(23).compile(), '{23}')


class TestRange(unittest.TestCase):
    def test_compile(self):
        self.assertEqual(Range((23, 27)).compile(), '{23,27}')

