#!/usr/bin/env python3

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


class Group(object):

    """ The class that represents one group

        Parameters
        ----------
        people : List[Person]
            The list of people in the group

        Attributes
        ----------
        answers : Set[str]
            The set of questions the group answered yes to

    """

    def __init__(self, people: List[Person]) -> None:
        answers: Set[str] = set()
        for person in people:
            answers.update(person.answers)
        self.answers = answers

    def __repr__(self) -> str:
        return f"<Group questions={self.answers}>"



def day06(file: str) -> int:
    """ Solves advent of code day06 """
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
    return sum(len(g.answers) for g in groups)


if __name__ == "__main__":
    results_test1 = day06("test.txt")
    print(results_test1)
