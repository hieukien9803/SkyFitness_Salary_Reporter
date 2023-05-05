from __future__ import annotations
from typing import List


class Employee:
    """
    An employee of the company

    This class is abstract; subclasses must implement get_commission()
    and get_fixed_salary().

    === Attributes ===
    fixed_salary: The amount of money an employee would get
    if worked enough work_day.
    work_day: The amount of work day that the employee wishes to work
    for a month.

    === Private Attributes ===
    _name: Name of the employee
    _birth: Date of birth of the employee
    _date_enter_company: The date that this employee enters the company
    _position: The position the employee is working at
    _status: The status of position the employee is currently working

    Note: All employee will have these specific attribute, but each of them
    might have a new attributes depends on what type of employee are they.

    === Representation invariants ===
    fixed_salary and work_day would never non-negative numbers.
    """
    _name: str
    _birth: str
    _date_enter_company: str
    _position: int
    _status: int
    day_off: int
    expected_work_day: float
    bank: str
    bank_name: str

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize an employee with name, birth, and fixed_salary

        Precondition: fixed_salary and work_day must be non-negative integers
        """
        self.name = name
        self._birth = birth
        self._date_enter_company = date_enter_company
        self.position = position
        self.status = status
        self.day_off = day_off
        self.expected_work_day = expected_work_day
        self.bank = bank
        self.bank_name = bank_name

    def __str__(self) -> str:
        """
        Print function for employee for testing purposes
        :return: none
        """
        return 'Employee(name=' + str(self.name) +\
               ', birth=' + str(self._birth) + ', date_enter_company=' + str(self._date_enter_company) \
               + ', position=' + str(self.position) + ', status=' + str(self.status) + ', day_off=' + str(self.day_off) + \
               ', expected_work_day=' + str(self.expected_work_day) + ', bank=' + str(self.bank) + ', bank_name=' + str(self.bank_name)

    def get_commission(self, performance) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager)
        """
        raise NotImplementedError("Implemented in a subclass")

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist, Janitor, Security)
        """
        raise NotImplementedError("Implemented in a subclass")

    def get_total_salary(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist, Janitor, Security)
        """
        raise NotImplementedError("Implemented in a subclass")

    def get_team_bonus(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist)
        """
        raise NotImplementedError("Implemented in a subclass")
