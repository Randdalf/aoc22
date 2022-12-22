#!/usr/bin/env python

"""Advent of Code 2022, Day 22"""

import re

from aoc import solve


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse_board(data):
    print(data)


def parse_path(data):
    for instr in re.findall(r'(\d+|L|R)', data):
        try:
            yield int(instr)
        except ValueError:
            yield instr


def parse_board(data):
    board = {}
    for y, row in enumerate(data.split('\n'), 1):
        for x, tile in enumerate(row, 1):
            if tile == ' ':
                continue
            board[(x, y)] = tile
    return board


def parse(data):
    board, path = data.split('\n\n')
    return parse_board(board), list(parse_path(path))


def final_password(notes):
    board, path = notes
    px, py = min((x, y) for x, y in board if y == 1)
    facing = 0
    for instr in path:
        if isinstance(instr, int):
            dx, dy = dirs[facing]
            for step in range(instr):
                nx, ny = px + dx, py + dy
                tile = board.get((nx, ny))
                if tile is None:
                    while (nx - dx, ny - dy) in board:
                        nx, ny = nx - dx, ny - dy
                    tile = board[(nx, ny)]
                if tile == '#':
                    break
                px, py = nx, ny
        elif instr == 'L':
            facing = (facing - 1) % len(dirs)
        else:
            facing = (facing + 1) % len(dirs)
    return 1000 * py + 4 * px + facing


if __name__ == "__main__":
    solve(22, parse, final_password)
