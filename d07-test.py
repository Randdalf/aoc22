#!/usr/bin/env python

"""Advent of Code 2022, Day 7 (Unit Tests)"""

import unittest

from d07 import parse, total_size, free_space

example1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class TotalSizeTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(total_size(parse(example1)), 95437)


class FreeSpaceTest(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(free_space(parse(example1)), 24933642)


if __name__ == "__main__":
    unittest.main()
