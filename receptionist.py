from __future__ import annotations
from employee import Employee
from monitor import get_actual_day_of_work
import pandas as pd


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
        self.file = get_receptionist_logic()
        self._fixed_salary = self.file.get(status)

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
        salary = day_of_work * (self._fixed_salary / self.expected_work_day)
        return salary

    def get_total_salary(self) -> float:
        """
        Return the *final* salary of this person
        :return:
        """
        cc = get_actual_day_of_work()
        day_of_w = cc.get(self.name) + self.day_off
        num = self.get_fixed_salary(day_of_work=day_of_w)
        return num

    def get_team_bonus(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist)
        """
        pass


def get_receptionist_logic() -> dict:
    """

    :return:
    """
    re_file = pd.read_excel('logic-file/receptionist-logic.xlsx')
    re_f = pd.DataFrame(re_file, columns=['Vị Trí', 'Lương cơ bản'])
    re_logic = {}

    for index, row in re_f.iterrows():
        if str(row['Vị Trí']).lower() != 'nan':
            re_logic[row['Vị Trí']] = int(row['Lương cơ bản'])

    return re_logic



