#!/usr/bin/env python3


import re
from typing import Dict, List


class Passport:
    """ Class for recording passport information """

    _req_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }

    def __init__(self, field_data: Dict[str, str]) -> None:
        self._field_data = field_data

    @staticmethod
    def is_valid_datatype(value: str, field: str) -> bool:
        """ Check if value is valid for the required field """
        if field == "byr":
            try:
                if (int(value) < 1920) or (int(value) > 2002):
                    return False
            except ValueError:
                return False
            return True
        if field == "iyr":
            try:
                if (int(value) < 2010) or (int(value) > 2020):
                    return False
            except ValueError:
                return False
            return True
        if field == "eyr":
            try:
                if (int(value) < 2020) or (int(value) > 2030):
                    return False
            except ValueError:
                return False
            return True
        if field == "hgt":
            if (not value.endswith("cm")) and (not value.endswith("in")):
                return False
            try:
                if value.endswith("cm"):
                    value = value.strip("cm")
                    if (int(value) < 150) or (int(value) > 193):
                        return False
                if value.endswith("in"):
                    value = value.strip("in")
                    if (int(value) < 59) or (int(value) > 76):
                        return False
            except ValueError:
                return False
            return True
        if field == "hcl":
            pattern = re.compile(r"^#[0-9a-f]{6}$")
            if not pattern.match(value):
                return False
            return True
        if field == "ecl":
            pattern = re.compile(r"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$")
            if not pattern.match(value):
                return False
            return True
        if field == "pid":
            pattern = re.compile(r"^[0-9]{9}$")
            if not pattern.match(value):
                return False
            return True
        raise ValueError("None of the required fields match")

    def is_valid(self, check_datatype: bool) -> bool:
        """ Check if passport is valid """
        validity = True
        if len(self._field_data) < 7:
            return False
        for req_field in self._req_fields:
            if req_field not in self._field_data.keys():
                return False
            if check_datatype:
                if not self.is_valid_datatype(self._field_data[req_field], req_field):
                    return False
        return validity


def day04(file: str, check_datatype: bool = False) -> int:
    """ Solves advent of code: day04 """
    passport_list = []
    with open(file) as fid:
        passport_item: Dict[str, str] = {}
        for line in fid:
            if line.strip() == "":
                passport = Passport(passport_item)
                passport_list.append(passport)
                passport_item = {}
            else:
                for field in line.strip().split(" "):
                    key, value = field.strip().split(":")
                    passport_item[key] = value
    return sum(passport.is_valid(check_datatype) for passport in passport_list)


if __name__ == "__main__":
    results_test1 = day04("test.txt")
    results_part1 = day04("input.txt")
    print(f"Results of part1: Test={results_test1}, Part1={results_part1}")
    results_test2 = day04("test.txt", check_datatype=True)
    results_part2 = day04("input.txt", check_datatype=True)
    print(f"Results of part2: Test={results_test2}, Part2={results_part2}")
