from __future__ import annotations

from employee import Employee
from company import get_pt_logic_file


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
    _teaching_percentage: float
    _sale_percentage: float

    def __init__(self, name: str, birth: str, date_enter_company: str,
                 position: int, status: int, expected_work_day: float,
                 teaching_percentage: float, sale_percentage: float,
                 day_off: int, bank: int, bank_name: str) -> None:
        """
        Initialize a personal trainer

        Precondition: fixed_salary must be a non-negative float
        """
        super().__init__(name, birth, date_enter_company, position, status,
                         expected_work_day, day_off, bank, bank_name)

        # find the initial base salary of this pt
        self.file = get_pt_logic_file()
        salary = self.file.get(position)
        self._fixed_salary = salary.get('base')

        self._teaching_percentage = teaching_percentage
        self._sale_percentage = sale_percentage

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
                if performance < int(num[0]):
                    percent_base = logic[i][1]
                    percent_contract = logic[i][2]
            elif '-' in logic[i][0]:
                num = logic[i][0].split("-")
                if int(num[0]) <= performance < int(num[1]):
                    percent_base = logic[i][1]
                    percent_contract = logic[i][2]
            elif '>' in logic[i][0]:
                num = logic[i][0].split('>')
                if performance > int(num[0]):
                    percent_base = logic[i][1]
                    percent_contract = logic[i][2]

        if percent_contract > 0:
            num = (percent_base * percent_contract) / 100
        else:
            num = percent_base / 100
        return num

    def get_fixed_salary(self, day_of_work: float) -> float:
        """
        Get the final fixed salary for this personal trainer according to the
        pt actual attendance versus their expected attendance
        :return: float
        """
        salary = (day_of_work / self.expected_work_day) * self._fixed_salary
        return salary

    def get_team_bonus(self) -> float:
        """
        During the month that personal trainers would together effectively
        that bring high sales for the company, they get bonus salary
        """
        pass
