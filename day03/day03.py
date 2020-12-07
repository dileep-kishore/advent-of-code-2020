#!/usr/bin/env python3

from math import prod
from typing import Iterable, List, Tuple


class Forest:
    """
    The `Forest` class

    Parameters
    ----------
    forest_seed : List[str]
        The seed pattern for the forest

    Attributes
    ----------
    forest : List[List[str]]
        The forest
    """

    def __init__(self, forest_seed: List[str]) -> None:
        self._dims = (len(forest_seed), len(forest_seed[0]))
        self.forest = self.build_forest(forest_seed)

    def build_forest(self, seed: List[str]) -> List[List[str]]:
        """
        Build forest from the given forest seed

        Parameters
        ----------
        seed : List[str]
            The seed pattern for the forest

        Returns
        -------
        List[Iterable]
            The forest
        """
        forest = [list(row) for row in seed]
        return forest

    def __getitem__(self, pos: Tuple[int, int]) -> str:
        """ Returns the value at `pos` in forest. Either '.' or '#' """
        row_num = pos[0]
        if pos[1] >= self._dims[1]:
            col_num = pos[1] % self._dims[1]
        else:
            col_num = pos[1]
        return self.forest[row_num][col_num]

    def is_valid_pattern(self, pattern: List[Tuple[str, int]]) -> bool:
        """ Check if pattern is valid """
        direction_set = {"up", "down", "left", "right"}
        for direction, value in pattern:
            if direction not in direction_set:
                return False
            elif not isinstance(value, int):
                return False
        return True

    def make_move(
        self, pos: Tuple[int, int], direction: str, move_value: int
    ) -> Tuple[int, int]:
        """
        Move in the forest in a particular direction

        Parameters
        ----------
        pos : Tuple[int, int]
            Starting position of the move
        direction : str
            The direction of the move
            Can be {"up", "down", "left", "right"}
        move_value : int
            The number of places to move

        Returns
        -------
        new_pos : Tuple[int, int]
            The new position after the move
        """
        new_pos = list(pos)
        if direction in {"left", "right"}:
            var_ind = 1
        else:
            var_ind = 0
        if move_value >= 0:
            new_pos[var_ind] += move_value
        else:
            new_pos[var_ind] -= move_value
        return tuple(new_pos)

    def traverse(self, pattern: List[Tuple[str, int]]) -> Iterable:
        """
        Traverse the forest

        Parameters
        ----------
        pattern : List[Tuple[str, int]]
            The traversal pattern: [(direction, value), ...]
            Valid directions: ['up', 'down', 'left', 'right']

        Returns
        -------
        Iterable
            (# of trees, current position)
        """
        num_trees = 0
        if not self.is_valid_pattern(pattern):
            raise ValueError(f"Invalid pattern {pattern}")
        pos: Tuple[int, int] = (0, 0)  # row, col
        while pos[0] < (self._dims[0] - 1):
            assert pos[0] >= 0 and pos[1] >= 0, "Invalid indices"
            for direction, move_value in pattern:
                new_pos = self.make_move(pos, direction, move_value)
                pos = new_pos
            if self[new_pos] == "#":
                num_trees += 1
            yield num_trees, new_pos


def day03(file: str, pattern: List[Tuple[str, int]]) -> int:
    """ Solves advent of code: day03 """
    with open(file) as fid:
        data = [l.strip() for l in fid.readlines()]
    forest = Forest(data)
    traversal = list(forest.traverse(pattern))
    return traversal[-1][0]


if __name__ == "__main__":
    results_test1 = day03("test.txt", [("right", 3), ("down", 1)])
    results_part1 = day03("input.txt", [("right", 3), ("down", 1)])
    print(f"Results of part1: Test={results_test1}, Part1={results_part1}")
    # Part 2
    part2_patterns = [
        [("right", 1), ("down", 1)],
        [("right", 3), ("down", 1)],
        [("right", 5), ("down", 1)],
        [("right", 7), ("down", 1)],
        [("right", 1), ("down", 2)],
    ]
    results_test2 = prod([day03("test.txt", pat) for pat in part2_patterns])
    results_part2 = prod([day03("input.txt", pat) for pat in part2_patterns])
    print(f"Results of part2: Test={results_test2}, Part2={results_part2}")
