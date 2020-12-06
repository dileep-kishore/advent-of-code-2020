#!/usr/bin/env python3

import itertools


def day01_part1(file: str):
    """ Solves advent of code: day01 part1 """
    with open(file) as fid:
        data = [int(line) for line in fid.readlines()]
    for n1, n2 in itertools.combinations(data, 2):
        if n1 + n2 == 2020:
            return n1 * n2


def day01_part2(file: str):
    """ Solves advent of code: day01 part2 """
    with open(file) as fid:
        data = [int(line) for line in fid.readlines()]
    for n1, n2, n3 in itertools.combinations(data, 3):
        if n1 + n2 + n3 == 2020:
            return n1 * n2 * n3


if __name__ == "__main__":
    result_test1 = day01_part1("test.txt")
    result_part1 = day01_part1("input.txt")
    result_test2 = day01_part2("test.txt")
    result_part2 = day01_part2("input.txt")
    print(f"Result of part1: Test={result_test1}, Input={result_part1}")
    print(f"Result of part2: Test={result_test2}, Input={result_part2}")
