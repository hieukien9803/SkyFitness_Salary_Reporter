from __future__ import annotations
from openpyxl import load_workbook
import pandas


from typing import List


class Monitor:
    """
    This class will monitor the time each employee worked for a day
    - Keep track of check in and check out time to check whether they
    made the shift in time.

    === Attributes ===
    date: This is the date that the employee is work
    start_time: This is the time the employee checked in
    end_time: This is the time the employee checked out
    shift: This is the time the employee have to check in

    === Representation invariants ===
    n/a
    """
    date: str
    start_time: str
    end_time: str
    shift: str

    def __init__(self, date: str, start_time: str, end_time: str,
                 shift: str) -> None:
        """
        Initialize a monitor for a da
        """
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.shift = shift

    def get_work_day(self) -> float:
        """
        Get the number of work that the employer worked whether he/she finish
        the work day

        If he/she didn't late for the sift, return 1
        If he/she late 10 min after the shift, return 0.8
        Note: this logic is based on the Company
        """


def read_late_policy_file(filename: str) -> None:
    """
    Read the Late Policy file given by the company

    filename: The name of a file that contains the deduction rate if the
    employee is late from the shift.
    """
    pass

def translate_range() -> bool:
    """
    Given a string of arithmetic equation and
    """


def read_work_day_file(filename: str) -> None:
    """
    Read the Employee file given by the company

    Precondition: the file stored at <filename> is in the format specified
    by the company.

    filename: The name of a file that contains the list of employees.
    """
    employees = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

