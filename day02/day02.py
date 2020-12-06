#!/usr/bin/env python3

from collections import Counter
from typing import Tuple


class Password:
    """
    The `Password` class
    Could store invalid passwords

    Parameters
    ----------
    password_string : str

    Attributes
    ----------
    policy : str
        The policy
    password : str
        The password
    """

    def __init__(self, password_string: str) -> None:
        policy, password = self._parse_string(password_string)
        self.policy = policy
        self.password = password

    @staticmethod
    def _parse_string(password_string: str) -> Tuple[Tuple[int, int, str], str]:
        """
        Parse the password string into policy and password

        Parameters
        ----------
        password_string : string

        Returns
        -------
        Tuple[str, str]
            Policy and password
        """
        policy_string, password = password_string.strip().split(": ")
        policy_string_limits, policy_string_char = policy_string.split(" ")
        lb, ub = policy_string_limits.split("-")
        policy = (int(lb), int(ub), policy_string_char)
        return policy, password

    def is_valid(self, part: str) -> bool:
        """ Validate password for the given policy """
        lb, ub, char = self.policy
        if part == "part1":
            password_counter = Counter(self.password)
            if char in password_counter:
                if lb <= password_counter[char] <= ub:
                    return True
                else:
                    return False
            else:
                return False
        elif part == "part2":
            pos1, pos2 = lb - 1, ub - 1
            if self.password[pos1] == char:
                if self.password[pos2] != char:
                    return True
                else:
                    return False
            elif self.password[pos2] == char:
                return True
            else:
                return False
        else:
            raise ValueError("Invalid part specified")


def day02(file: str, part: str) -> int:
    with open(file) as fid:
        passwords = [Password(line) for line in fid.readlines()]
    valid_password_count = sum([password.is_valid(part) for password in passwords])
    return valid_password_count


if __name__ == "__main__":
    results_test1 = day02("test.txt", "part1")
    results_part1 = day02("input.txt", "part1")
    print(f"Results of part1: Test={results_test1}, Part1={results_part1}")
    results_test2 = day02("test.txt", "part2")
    results_part2 = day02("input.txt", "part2")
    print(f"Results of part2: Test={results_test2}, Part2={results_part2}")
