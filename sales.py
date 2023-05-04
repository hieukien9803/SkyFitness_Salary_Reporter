from __future__ import annotations
from employee import Employee
from monitor import Monitor
from company import get_sale_logic_file
import pandas as pd


class Sale(Employee):
    """
    A sale person

    === Private Attributes ===
    _name: Name of the employee
    _birth: Date of birth of the employee
    _fixed_salary: The amount of money an employee would get
    if worked enough hrs

    === Representation invariants ===
    fixed_salary and work_day are non-negative numbers.
    """

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: int, bank_name: str) -> None:
        """
        Initialize an employee with name, birth, and fixed_salary

        Precondition: fixed_salary and work_day must be non-negative numbers.
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)

        self.file = get_sale_logic_file()
        salary = self.file.get(position)
        self._fixed_salary = salary.get('base')

    def get_commission(self, performance) -> float:
        """
        Get the commission for a sale depends on the performance
        performance: the amount of money the sale made this month
        """
        lg = self.file.get(self.position)
        logic = lg.get('logic')
        percent = 0
        bonus = 0
        for i in range(len(logic)):
            if '<' in logic[i][0]:
                num = logic[i][0].split('<')
                if performance < int(num[0]):
                    percent = logic[i][1]
                    bonus = logic[i][2]
            elif '-' in logic[i][0]:
                num = logic[i][0].split("-")
                if int(num[0]) <= performance < int(num[1]):
                    percent = logic[i][1]
                    bonus = logic[i][2]
            elif '>' in logic[i][0]:
                num = logic[i][0].split('>')
                if performance > int(num[0]):
                    percent = logic[i][1]
                    bonus = logic[i][2]

        if bonus > 0:
            num = (percent * bonus) / 100
        else:
            num = percent / 100
        return num

    def get_fixed_month_salary(self, day_of_work: float) -> float:
        """
        Get the total salary of one month for a sale person

        day_of_work: the actual amount of days the sale person
        worked for a month
        """
        salary = (day_of_work / self.expected_work_day) * self._fixed_salary
        return salary

    def get_total_salary(self) -> float:
        """
        Return the total salary of this sale
        :return: float
        """
        num = self.get_fixed_month_salary(day_of_work=)
        num2 = self.get_commission(performance=)
        return num * num2

    def get_team_bonus(self) -> float:
        """
        Get the team bonus salary if applicable according to the logic file
        """
        pass
