import unittest


class PatternTestCase(unittest.TestCase):
    def assert_matches(self, pattern, candidate):
        return self.assertRegexpMatches(candidate, pattern.compile())

    def assert_doesnt_match(self, pattern, candidate):
        return self.assertNotRegexpMatches(candidate, pattern.compile())

