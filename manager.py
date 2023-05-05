from __future__ import annotations
from employee import Employee

from typing import List


class Manager(Employee):
    """
    A manager of the company

    === Attributes ===
    n/a

    === Private Attributes ===
    Inherited from Employee() class

    === Representation invariants ===
    _fixed_salary would never be negative
    """

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize an employee with name, birth, and fixed_salary

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)

    def get_commission(self, performance) -> float:
        """
        Get the commission for the manager depends on his performance

        """
        pass

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist, Janitor, Security)
        """
        return self.fixed_salary * day_of_work

    def get_team_bonus(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist)
        """
        pass
