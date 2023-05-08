from __future__ import annotations

from monitor import get_actual_day_of_work, get_performance_report, split_list
from employee import Employee
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
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize an employee with name, birth, and fixed_salary

        Precondition: fixed_salary and work_day must be non-negative numbers.
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)

        self.file = get_sale_logic_file()
        salary = self.file.get(status)
        self._fixed_salary = salary.get('base')

    def get_commission(self, performance: float) -> float:
        """
        Get the commission for a sale depends on the performance
        performance: the amount of money the sale made this month
        """
        lg = self.file.get(self.status)
        logic = lg.get('logic')
        percent = 0
        bonus = 0
        for i in range(len(logic)):
            if '<' in logic[i][0]:
                num = logic[i][0].split('<')
                if performance < float(num[1])*1000000:
                    percent = logic[i][1]
                    bonus = logic[i][2]
            elif '-' in logic[i][0]:
                num = logic[i][0].split("-")
                if float(num[0])*1000000 <= performance < float(num[1])*1000000:
                    percent = logic[i][1]
                    bonus = logic[i][2]
            elif '>' in logic[i][0]:
                num = logic[i][0].split('>')
                if performance > float(num[1])*1000000:
                    percent = logic[i][1]
                    bonus = logic[i][2]

        if bonus > 0:
            num = (percent * (bonus/100)) / 100
        else:
            num = percent / 100
        return num

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Get the total salary of one month for a sale person

        day_of_work: the actual amount of days the sale person
        worked for a month
        """
        salary = day_of_work * (self._fixed_salary / self.expected_work_day)
        print('fixed = ' + str(self._fixed_salary))
        print('expected work = ' + str(self.expected_work_day))
        print('actual day = ' + str(day_of_work))
        print(salary)
        return salary

    def get_total_salary(self) -> float:
        """
        Return the *final* salary of this sale
        :return: float
        """
        cc = get_actual_day_of_work()
        pp = get_performance_report()

        day_of_w = cc.get(self.name)
        performance = pp.get(self.name)

        num = self.get_fixed_salary(day_of_work=day_of_w)
        num2 = self.get_commission(performance=performance)
        return num + (performance * num2)

    def get_team_bonus(self) -> float:
        """
        Get the team bonus salary if applicable according to the logic file
        """
        pass


def get_sale_logic_file() -> dict:
    """
    Translate input from csv file to tuple for standard calculation for sale
    salary.
    """
    sl_file = pd.read_excel('logic-file/sale-logic.xlsx')
    sl_f = pd.DataFrame(sl_file, columns=['Vị Trí', 'Lương cơ bản', 'Doanh Thu',
                                          '% lương cơ bản',
                                          '% hoa hồng sale đã bán'])
    sl_logic = {}

    sale1 = sl_f.loc[0:4, ['Doanh Thu',
                           '% lương cơ bản',
                           '% hoa hồng sale đã bán']].values.flatten().tolist()
    sale2 = sl_f.loc[5:9, ['Doanh Thu',
                           '% lương cơ bản',
                           '% hoa hồng sale đã bán']].values.flatten().tolist()
    sale3 = sl_f.loc[10:14, ['Doanh Thu',
                             '% lương cơ bản',
                             '% hoa hồng sale đã bán']].values.flatten().tolist()
    sale4 = sl_f.loc[15:19, ['Doanh Thu',
                             '% lương cơ bản',
                             '% hoa hồng sale đã bán']].values.flatten().tolist()
    sale5 = sl_f.loc[20:25, ['Doanh Thu',
                             '% lương cơ bản',
                             '% hoa hồng sale đã bán']].values.flatten().tolist()

    s1 = split_list(sale1, 3)
    s2 = split_list(sale2, 3)
    s3 = split_list(sale3, 3)
    s4 = split_list(sale4, 3)
    s5 = split_list(sale5, 3)

    for index, row in sl_f.iterrows():
        if str(row['Vị Trí']).lower() != 'nan':
            if int(row['Vị Trí']) == 1:
                sale = {'base': float(row['Lương cơ bản']), 'logic': s1}
                sl_logic[int(row['Vị Trí'])] = sale
            elif int(row['Vị Trí']) == 2:
                sale = {'base': float(row['Lương cơ bản']), 'logic': s2}
                sl_logic[int(row['Vị Trí'])] = sale
            elif int(row['Vị Trí']) == 3:
                sale = {'base': float(row['Lương cơ bản']), 'logic': s3}
                sl_logic[int(row['Vị Trí'])] = sale
            elif int(row['Vị Trí']) == 4:
                sale = {'base': float(row['Lương cơ bản']), 'logic': s4}
                sl_logic[int(row['Vị Trí'])] = sale
            elif int(row['Vị Trí']) == 5:
                sale = {'base': float(row['Lương cơ bản']), 'logic': s5}
                sl_logic[int(row['Vị Trí'])] = sale

    return sl_logic
