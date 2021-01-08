#!/usr/bin/env python3

from collections import Counter
from typing import List, Set


class Person:

    """The class the represnts one person

    Parameters
    ----------
    question_string : str
        The string of questions that the person answered "yes" to

    Attributes
    ----------
    answers : Set[str]
        The set of questions the person answered yes to
    """

    def __init__(self, question_string: str) -> None:
        answers = set(question_string)
        self.answers = answers

    def __repr__(self) -> str:
        return f"<Person questions={self.answers}>"


class Group:

    """The class that represents one group

    Parameters
    ----------
    people : List[Person]
        The list of people in the group

    Attributes
    ----------
    size : int
        The number of people in the group
    answer_count : Dict[str, int]
        The questions people in the group answered and their count

    """

    def __init__(self, people: List[Person]) -> None:
        self.size = len(people)
        all_answers: List[str] = []
        for person in people:
            all_answers.extend(list(person.answers))
        self.answer_count = Counter(all_answers)

    def __repr__(self) -> str:
        return f"<Group questions={list(self.answer_count.keys())}>"

    @property
    def unanimous(self) -> List[str]:
        """ The questions everyone answered yes to """
        unanimous_answers: List[str] = []
        for key, value in self.answer_count.items():
            if value == self.size:
                unanimous_answers.append(key)
        return unanimous_answers


def day06(file: str, part: str) -> int:
    """ Solves advent of code day06 part 2 """
    groups: List[Group] = []
    curr_group: List[Person] = []
    with open(file) as fid:
        for line in fid:
            if line.strip():
                person = Person(line.strip())
                curr_group.append(person)
            else:
                if curr_group:
                    group = Group(curr_group)
                    groups.append(group)
                    curr_group: List[Person] = []
    if part == "part1":
        return sum(len(g.answer_count) for g in groups)
    elif part == "part2":
        return sum(len(g.unanimous) for g in groups)
    else:
        raise ValueError("Part can either be part1 or part2")


if __name__ == "__main__":
    results_test1 = day06("test.txt", "part1")
    results_part1 = day06("input.txt", "part1")
    print(f"Results of part1: Test={results_test1}, Part1={results_part1}")
    results_part2 = day06("input.txt", "part2")
    print(f"Results of part2: Part2={results_part2}")
