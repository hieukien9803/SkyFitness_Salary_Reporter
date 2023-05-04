from __future__ import annotations

from employee import Employee


class Janitor(Employee):
    """
    A janitor class

    Janitor's salary is based on the fixed_salary and day_of_work
    === Attributes ===
    Inherited from Employee() class

    === Representation invariants ===
    fixed_salary and work_day are non-negative numbers
    """

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: str, status: int, fixed_salary: int,
                 work_day: float) -> None:
        """
        Initialize the janitor

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         fixed_salary, work_day)

    def get_commission(self) -> float:
        """
        Janitor does not have commission salary, return 0.0
        """
        return 0.0

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Get the total salary of one month for the janitor

        day_of_work: the amount of days the janitor worked for a month
        """
        return self.fixed_salary * day_of_work
