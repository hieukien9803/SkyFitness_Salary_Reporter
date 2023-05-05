from __future__ import annotations
from employee import Employee
from monitor import get_actual_day_of_work


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
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize the receptionist

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)
        self.fixed_salary = 4500000.0

    def get_commission(self, performance) -> float:
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
        total_day_of_work = day_of_work / self.expected_work_day
        salary = total_day_of_work * self.fixed_salary
        return salary

    def get_total_salary(self) -> float:
        """
        Return the *final* salary of this person
        :return:
        """
        cc = get_actual_day_of_work()
        day_of_w = cc.get(self.name)
        num = self.get_fixed_salary(day_of_work=day_of_w)
        return num

    def get_team_bonus(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist)
        """
        pass
