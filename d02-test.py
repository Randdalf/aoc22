#!/usr/bin/env python

"""Advent of Code 2022, Day 2 (Unit Tests)"""

import unittest

from d02 import parse, encrypted_guide, decrypted_guide

example1 = """A Y
B X
C Z"""


class EncryptedGuideTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(encrypted_guide(parse(example1)), 15)


class DecryptedGuideTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(decrypted_guide(parse(example1)), 12)


if __name__ == "__main__":
    unittest.main()
