from __future__ import annotations
from employee import Employee

from typing import List
import pandas as pd
from monitor import split_list, get_actual_day_of_work, get_performance_report

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
        self.file = get_manager_logic_file()
        self.fixed_salary = self.file.get('base')
        self.logic = self.file.get('logic')

    def get_commission(self, performance) -> float:
        """
        Get the commission for the manager depends on his performance

        """
        percent_base = 0
        bonus = 0
        for i in range(len(self.logic)):
            if '<' in self.logic[i][0]:
                num = self.logic[i][0].split('<')
                if performance < float(num[1])*1000000:
                    bonus = self.logic[i][2]
                    percent_base = self.logic[i][3]
            elif '-' in self.logic[i][0]:
                num = self.logic[i][0].split("-")
                if float(num[0])*1000000 <= performance < float(num[1])*1000000:
                    bonus = self.logic[i][2]
                    percent_base = self.logic[i][3]
            elif '>' in self.logic[i][0]:
                num = self.logic[i][0].split('>')
                if performance > float(num[1])*1000000:
                    bonus = self.logic[i][2]
                    percent_base = self.logic[i][3]

        if bonus > 0:
            num = (performance * (bonus/100)) + (self.fixed_salary * percent_base)
        else:
            num = self.fixed_salary * percent_base
        return num

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Return the number of fixed salary for the month
        """
        return (self.fixed_salary / self.expected_work_day) * day_of_work

    def get_total_salary(self) -> float:
        """

        :return:
        """
        pass

    def get_team_bonus(self) -> float:
        """
        This function should be implemented in the subclasses.
        (ie. PT, Sale, Manager, Receptionist)
        """
        pass


def get_manager_logic_file() -> dict:
    """

    :return:
    """
    manager_file = pd.read_excel('logic-file/manager-logic.xlsx')
    ma_f = pd.DataFrame(manager_file,
                        columns=['Lương cơ bản', 'Tháng cao điểm (3-12)',
                                 'Tháng thấp điểm (1-2)',
                                 '% Doanh số', '% lương CB'])
    ma = ma_f.loc[0:4, ['Tháng cao điểm (3-12)',
                           'Tháng thấp điểm (1-2)',
                           '% Doanh số', '% lương CB']].values.flatten().tolist()
    m = split_list(ma, 4)
    ma_logic = {}
    for index, row in ma_f.iterrows():
        if str(row['Lương cơ bản']).lower() != 'nan':
            ma_logic['base'] = float(row['Lương cơ bản'])
            ma_logic['logic'] = m

    return ma_logic

