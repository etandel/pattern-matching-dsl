from pattern.char_classes import CHAR, LETTER, UPPER, LOWER, DIGIT

from .base import PatternTestCase


class TestCharClass(PatternTestCase):
    def test_char(self):
        self.assert_matches(CHAR, 'a')
        self.assert_matches(CHAR, 'A')
        self.assert_matches(CHAR, 'h')
        self.assert_matches(CHAR, 'H')
        self.assert_matches(CHAR, '1')
        self.assert_matches(CHAR, '.')
        self.assert_matches(CHAR, '_')

    def test_letter(self):
        self.assert_matches(LETTER, 'a')
        self.assert_matches(LETTER, 'A')
        self.assert_matches(LETTER, 'h')
        self.assert_matches(LETTER, 'H')

        self.assert_doesnt_match(LETTER, '1')
        self.assert_doesnt_match(LETTER, '.')
        self.assert_doesnt_match(LETTER, '_')

    def test_upper(self):
        self.assert_matches(UPPER, 'A')
        self.assert_matches(UPPER, 'H')

        self.assert_doesnt_match(UPPER, 'a')
        self.assert_doesnt_match(UPPER, 'h')
        self.assert_doesnt_match(UPPER, '1')
        self.assert_doesnt_match(UPPER, '.')
        self.assert_doesnt_match(UPPER, '_')

    def test_upper(self):
        self.assert_matches(LOWER, 'a')
        self.assert_matches(LOWER, 'h')

        self.assert_doesnt_match(LOWER, 'A')
        self.assert_doesnt_match(LOWER, 'H')
        self.assert_doesnt_match(LOWER, '1')
        self.assert_doesnt_match(LOWER, '.')
        self.assert_doesnt_match(LOWER, '_')

    def test_digit(self):
        for i in range(10):
            self.assert_matches(DIGIT, str(i))

        self.assert_doesnt_match(DIGIT, 'a')
        self.assert_doesnt_match(DIGIT, 'A')
        self.assert_doesnt_match(DIGIT, 'H')
        self.assert_doesnt_match(DIGIT, 'h')
        self.assert_doesnt_match(DIGIT, '.')
        self.assert_doesnt_match(DIGIT, '_')

