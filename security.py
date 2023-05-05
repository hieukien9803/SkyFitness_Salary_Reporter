from __future__ import annotations

from monitor import get_actual_day_of_work
from employee import Employee


class Security(Employee):
    """
    A security class

    Security's salary is different from other employees since security is
    hour salary employee

    Security salary is based on the fixed_salary and the hour_of_work

    === Attributes ===
    Inherited from Employee() class

    === Representation invariants ===
    fixed_salary and work_day are non-negative numbers
    """

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize the receptionist

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)
        self.salary_per_hour = 19000.0

    def get_commission(self, performance) -> float:
        """
        Security does not have commission salary
        """
        return 0.0

    def get_fixed_salary(self, hour_of_work: float) -> float:
        """
        Get the total salary of one month for the security

        hour_of_work: the amount of hours the security worked for a month
        """
        return self.salary_per_hour * hour_of_work

    def get_total_salary(self) -> float:
        """

        :return:
        """
        cc = get_actual_day_of_work()
        dw = cc.get(self.name)
        num = self.get_fixed_salary(dw)
        return num
