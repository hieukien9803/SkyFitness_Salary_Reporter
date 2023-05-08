from __future__ import annotations

from monitor import get_performance_report, get_actual_day_of_work
from employee import Employee
import pandas as pd


class PersonalTrainer(Employee):
    """
    A personal trainer

    === Private Attributes ===
    Inherited from Employee() class
    _teaching_percentage: The percentage of money that the personal trainer
    get for each teaching class.
    _sale_percentage: The percentage of money that the personal trainer get for
    every one-on-one program sale they made.

    === Representation invariants ===
    fixed_salary and work_day are non-negative numbers
    """

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: int, status: int, expected_work_day: float,
                 day_off: int, bank: str, bank_name: str) -> None:
        """
        Initialize a personal trainer

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)

        # find the initial base salary of this pt
        self.file = get_pt_logic_file()
        salary = self.file.get(status)
        self._fixed_salary = salary.get('base')

    def get_commission(self, performance) -> float:
        """
        Get the commission for a personal trainer depends on the performance

        """
        lg = self.file.get(self.position)
        logic = lg.get('logic')
        percent_base = 0
        percent_contract = 0
        for i in range(len(logic)):
            if '<' in logic[i][0]:
                num = logic[i][0].split('<')
                if performance < int(num[1]):
                    percent_base = logic[i][1]
                    percent_contract = logic[i][2]
            elif '-' in logic[i][0]:
                num = logic[i][0].split("-")
                if int(num[0]) <= performance < int(num[1]):
                    percent_base = logic[i][1]
                    percent_contract = logic[i][2]
            elif '>' in logic[i][0]:
                num = logic[i][0].split('>')
                if performance > int(num[1]):
                    percent_base = logic[i][1]
                    percent_contract = logic[i][2]

        if percent_contract > 0:
            num = (percent_base / 100) * (percent_contract / 100)
        else:
            num = percent_base / 100
        return num

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Get the final fixed salary for this personal trainer according to the
        pt actual attendance versus their expected attendance
        :return: float
        """
        salary = day_of_work * (self._fixed_salary / self.expected_work_day)
        return salary

    def get_total_salary(self) -> float:
        """

        :return:
        """
        cc = get_actual_day_of_work()
        day_of_w = cc.get(self.name)
        print(day_of_w)
        pp = get_performance_report()
        performance = pp.get(self.name)
        num = self.get_fixed_salary(day_of_work=day_of_w)
        num2 = self.get_commission(performance=performance)
        return num + (performance * num2)

    def get_team_bonus(self) -> float:
        """
        During the month that personal trainers would together effectively
        that bring high sales for the company, they get bonus salary
        """
        pass


def split_list(lst, n):
    """Split a list into sublists containing n elements."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def get_pt_logic_file() -> dict:
    """
    Translate input from csv file to tuple for standard calculation for pt
    salary.
    """
    pt_file = pd.read_excel('logic-file/pt-logic.xlsx')
    pt_f = pd.DataFrame(pt_file,
                        columns=['Vị Trí', 'Lương cứng', 'Doach thu (triệu)',
                                 '% lương CB',
                                 '% bán HH',
                                 '0-40', '41-70', '71-100', '>100'])
    pt_logic = {}

    ptr1 = pt_f.loc[0:4, ['Doach thu (triệu)',
                          '% lương CB',
                          '% bán HH',
                          '0-40', '41-70', '71-100',
                          '>100']].values.flatten().tolist()
    ptr2 = pt_f.loc[5:9, ['Doach thu (triệu)',
                          '% lương CB',
                          '% bán HH',
                          '0-40', '41-70', '71-100',
                          '>100']].values.flatten().tolist()
    ptr3 = pt_f.loc[11:15, ['Doach thu (triệu)',
                            '% lương CB',
                            '% bán HH',
                            '0-40', '41-70', '71-100',
                            '>100']].values.flatten().tolist()

    pt1 = split_list(ptr1, 7)
    pt2 = split_list(ptr2, 7)
    pt3 = split_list(ptr3, 7)

    for index, row in pt_f.iterrows():
        if str(row['Vị Trí']).lower() != 'nan' and str(
                row['Vị Trí']).lower() != 'vị trí':
            if int(row['Vị Trí']) == 1:
                pt = {'base': float(row['Lương cứng']), 'logic': pt1}
                pt_logic[int(row['Vị Trí'])] = pt
            elif int(row['Vị Trí']) == 2:
                pt = {'base': float(row['Lương cứng']), 'logic': pt2}
                pt_logic[int(row['Vị Trí'])] = pt
            elif int(row['Vị Trí']) == 3:
                pt = {'base': float(row['Lương cứng']), 'logic': pt3}
                pt_logic[int(row['Vị Trí'])] = pt

    return pt_logic


def get_pt_price_session_report() -> dict:
    """
    Read the pt file report to see how much the pt teaches and how much
    each session cost
    :return: dict
    """
    pt_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx',
                            sheet_name='PT')
    pt_f = pd.DataFrame(pt_file,
                        columns=['Danh sách hội viên', 'Giá trị 1 buổi'])
    report = {}
    for index, row in pt_f.iterrows():
        if str(row['Giá trị 1 buổi']).lower() != 'nan':
            report[str(row['Danh sách hội viên']).replace(' ', '')] = float(
                row['Giá trị 1 buổi'])

    return report


def get_pt_month_session() -> dict:
    """

    :return:
    """
    pt_detail_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx',
                                   sheet_name='Chi Tiết PT')
    pt_detail_f = pd.DataFrame(pt_detail_file,
                               columns=['Đức', 'Hưng', 'Đồng', 'Hùng Anh',
                                        'SB1', 'SB2', 'SB3', 'SB4'])
    total_session = {}
    temp = []
    for index, row in pt_detail_f.iterrows():
        if str(row['Đức']).lower() != 'nan':
            if str(row['SB1']) != 'nan':
                temp.append(str(row['Đức']))
    total_session['Đức'] = temp

    temp = []
    for index, row in pt_detail_f.iterrows():
        if str(row['Hưng']).lower() != 'nan':
            if str(row['SB2']) != 'nan':
                temp.append(str(row['Hưng']))
    total_session['Hưng'] = temp

    temp = []
    for index, row in pt_detail_f.iterrows():
        if str(row['Đồng']).lower() != 'nan':
            if str(row['SB3']) != 'nan':
                temp.append(str(row['Đồng']))
    total_session['Đồng'] = temp

    temp = []
    for index, row in pt_detail_f.iterrows():
        if str(row['Hùng Anh']).lower() != 'nan':
            if str(row['SB4']) != 'nan':
                temp.append(str(row['Hùng Anh']))
    total_session['Hùng Anh'] = temp

    return total_session

# a = get_pt_month_session()
# print(a)
