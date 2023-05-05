from __future__ import annotations

from monitor import get_actual_day_of_work
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
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize the janitor

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)
        self.fixed_salary_per_day = 200000.0

    def get_commission(self, performance) -> float:
        """
        Janitor does not have commission salary, return 0.0
        """
        return 0.0

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Get the total salary of one month for the janitor

        day_of_work: the amount of days the janitor worked for a month
        """
        return self.fixed_salary_per_day * day_of_work

    def get_total_salary(self) -> float:
        """
        Get final salary of this person
        :return:
        """
        cc = get_actual_day_of_work()
        work_day = cc.get(self.name)
        num = self.get_fixed_salary(day_of_work=work_day)
        return num

