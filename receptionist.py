from __future__ import annotations
from employee import Employee


class Receptionist(Employee):
    """
    A receptionist

    Receptionist salary is based on the fixed_salary and the day_of_work
    === Attributes ===
    n/a

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
        Receptionist does not have commission salary
        """
        return 0.0

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Get the total salary of one month for the receptionist

        day_of_work: the actual amount of days the receptionist
        worked for a month
        """
        total_day_of_work = day_of_work / self.work_day
        salary = total_day_of_work * self.fixed_salary
        return salary

    def get_team_bonus(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist)
        """
        pass
