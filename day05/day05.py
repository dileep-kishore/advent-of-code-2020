#!/usr/bin/env python3

from typing import Dict, List, Tuple


class Seat:
    """
    Class that stores information about a seat

    Parameters
    ----------
    seat_string : str
        The seat string of the seat
    row_limit : int
        The number of rows in the seat string
    col_limit : int
        The number of cols in the seat string
    row_code: Dict[str, int]
        The row partition code for the string
        Default value {"F": -1, "B": 1}
    col_code: Dict[str, int]
        The col partition code for the string
        Default value {"L": -1, "R": 1}

    Attributes
    ----------
    string : str
        The seat string of the seat
    rows : int
        The max number of rows
    cols : int
        The max number of cols
    row_code : Dict[str, int]
        The row partition code for the string
    col_code : Dict[str, int]
        The col partition code for the string
    """

    def __init__(
        self,
        seat_string: str,
        row_limit: int = 7,
        col_limit: int = 3,
        row_code: Dict[str, int] = {"F": -1, "B": 1},
        col_code: Dict[str, int] = {"L": -1, "R": 1},
    ) -> None:
        self.string = seat_string
        self._row_limit = row_limit
        self._col_limit = col_limit
        self.rows = 2 ** self._row_limit
        self.cols = 2 ** self._col_limit
        self.row_code = row_code
        self.col_code = col_code

    @staticmethod
    def _binary_partition(
        string: str, array: List[int], partition_code: Dict[str, int]
    ) -> int:
        """
        Performs binary partitioning and returns the id in the array

        Parameters
        ----------
        string : str
            The string that encodes the partitioning information
        array : List[int]
            The array to be partioned
        partition_code : Dict[str, int]
            The code for the string encoding
            Value must be one of -1 or 1

        Returns
        -------
        int
            The required index in the array
        """
        sub_array = array
        for s in string:
            curr_size = len(sub_array)
            partition = partition_code[s]
            if partition > 0:
                sub_array = sub_array[curr_size // 2 :]
            else:
                sub_array = sub_array[: curr_size // 2]
        assert len(sub_array) == 1
        return sub_array[0]

    @property
    def location(self) -> Tuple[int, int]:
        """ Returns the row and column of the seat """
        row_array = [r for r in range(self.rows)]
        # NOTE: We assume that the row string is always first
        row_string = self.string[: self._row_limit]
        col_array = [c for c in range(self.cols)]
        col_string = self.string[self._row_limit : (self._row_limit + self._col_limit)]
        row_num = self._binary_partition(row_string, row_array, self.row_code)
        col_num = self._binary_partition(col_string, col_array, self.col_code)
        return row_num, col_num

    @property
    def number(self) -> int:
        """ Returns the seat number """
        row_num, col_num = self.location
        return row_num * self.cols + col_num


def day05_part1(file: str) -> int:
    """ Solves advent of code: day05 part1 """
    with open(file) as fid:
        seats = [Seat(line.strip()) for line in fid]
    highest_seat_num = max(seat.number for seat in seats)
    return highest_seat_num


def day05_part2(file: str) -> int:
    """ Solves advent of code: day05 part2 """
    with open(file) as fid:
        seat_nums = [Seat(line.strip()).number for line in fid]
    seat_nums.sort()
    for i in range(min(seat_nums), max(seat_nums)):
        if i not in seat_nums:
            return i
    raise ValueError("No missing seat number found")


if __name__ == "__main__":
    results_test1 = day05_part1("test.txt")
    results_part1 = day05_part1("input.txt")
    print(f"Results of part1: Test={results_test1}, Part1={results_part1}")
    results_part2 = day05_part2("input.txt")
    print(f"Results of part2: Part2={results_part2}")
