from __future__ import annotations

from itertools import islice
import pandas as pd
from typing import List
from employee import Employee
from sales import Sale
from pt import PersonalTrainer
from manager import Manager
from receptionist import Receptionist
from security import Security
from janitor import Janitor

"""
This module is responsible to write any report file for the clients
"""


def create_company_employee_salary_report() -> None:
    """
    Create a new excel file with report content about each employee's salary
    for the month and store it in report-file
    :return: none
    """
    table = pd.DataFrame(columns=['Họ và tên', 'Ngày bắt đầu làm việc', '', 'Hệ số',
                                  'Lương TB/ngày', 'Số làm việc TT', 'Nghỉ phép/lễ',
                                  'Tổng số ngày công', 'Thành tiền', 'Ghi chú'])
