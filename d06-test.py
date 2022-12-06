#!/usr/bin/env python

"""Advent of Code 2022, Day 6 (Unit Tests)"""

import unittest

from d06 import packet_start, message_start

example1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
example2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
example3 = "nppdvjthqldpwncqszvftbrmjlhg"
example4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


class PacketStartTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(packet_start(example1), 7)

    def test_example2(slf):
        slf.assertEqual(packet_start(example2), 5)

    def test_example3(slf):
        slf.assertEqual(packet_start(example3), 6)

    def test_example4(slf):
        slf.assertEqual(packet_start(example4), 10)

    def test_example5(slf):
        slf.assertEqual(packet_start(example5), 11)


class MessageStartTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(message_start(example1), 19)

    def test_example2(slf):
        slf.assertEqual(message_start(example2), 23)

    def test_example3(slf):
        slf.assertEqual(message_start(example3), 23)

    def test_example4(slf):
        slf.assertEqual(message_start(example4), 29)

    def test_example5(slf):
        slf.assertEqual(message_start(example5), 26)


if __name__ == "__main__":
    unittest.main()
