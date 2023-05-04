from __future__ import annotations

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
                 position: str, status: int, fixed_salary: int,
                 work_day: float) -> None:
        """
        Initialize the receptionist

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         fixed_salary, work_day)

    def get_commission(self) -> float:
        """
        Security does not have commission salary
        """
        return 0.0

    def get_fixed_salary(self, hour_of_work: float) -> float:
        """
        Get the total salary of one month for the security

        hour_of_work: the amount of hours the security worked for a month
        """
        return self.fixed_salary * hour_of_work
