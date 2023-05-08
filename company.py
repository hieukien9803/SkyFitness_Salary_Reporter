from __future__ import annotations

from itertools import islice
from monitor import get_actual_day_of_work, get_performance_report
import pandas as pd
from typing import List
from employee import Employee
from manager import Manager
from pt import PersonalTrainer
from sales import Sale
from receptionist import Receptionist
from janitor import Janitor
from security import Security


def create_employee_list() -> List[Employee]:
    """
    Read the Employee file give by the company, then create employees based
    on the file given

    Precondition: the file stored at <filename> is in the format specified
    by the company.
    """
    employees = []
    employ_file = pd.read_excel('input-file/employees_file.xlsx',
                                engine='openpyxl')
    e_file = pd.DataFrame(employ_file, columns=['Họ và Tên',
                                                'Ngày/Tháng/Năm sinh',
                                                'Ngày bắt đầu làm việc',
                                                'Chức vụ',
                                                'Vị trí',
                                                'Tổng số ngày công',
                                                'Nghỉ phép',
                                                'Tài khoản',
                                                'Ngân hàng'])
    for index, row in e_file.iterrows():
        if str(row['Họ và Tên']).lower() != 'nan':
            if int(row['Chức vụ']) == 1:
                employees.append(Manager(name=str(row['Họ và Tên']),
                                         birth=str(row['Ngày/Tháng/Năm sinh']),
                                         date_enter_company=str(
                                             row['Ngày bắt đầu làm việc']),
                                         position=int(row['Chức vụ']),
                                         status=int(row['Vị trí']),
                                         expected_work_day=int(
                                             row['Tổng số ngày công']),
                                         day_off=int(row['Nghỉ phép']),
                                         bank=str(row['Tài khoản']),
                                         bank_name=str(row['Ngân hàng'])
                                         ))
            elif int(row['Chức vụ']) == 2:
                employees.append(PersonalTrainer(name=str(row['Họ và Tên']),
                                                 birth=str(row[
                                                               'Ngày/Tháng/Năm sinh']),
                                                 date_enter_company=str(row[
                                                                            'Ngày bắt đầu làm việc']),
                                                 position=int(row['Chức vụ']),
                                                 status=int(row['Vị trí']),
                                                 expected_work_day=int(
                                                     row['Tổng số ngày công']),
                                                 day_off=int(row['Nghỉ phép']),
                                                 bank=str(row['Tài khoản']),
                                                 bank_name=str(row['Ngân hàng'])
                                                 ))
            elif int(row['Chức vụ']) == 3:
                employees.append(Sale(name=str(row['Họ và Tên']),
                                      birth=str(row['Ngày/Tháng/Năm sinh']),
                                      date_enter_company=str(
                                          row['Ngày bắt đầu làm việc']),
                                      position=int(row['Chức vụ']),
                                      status=int(row['Vị trí']),
                                      expected_work_day=int(
                                          row['Tổng số ngày công']),
                                      day_off=int(row['Nghỉ phép']),
                                      bank=str(row['Tài khoản']),
                                      bank_name=str(row['Ngân hàng'])
                                      ))
            elif int(row['Chức vụ']) == 4:
                employees.append(Receptionist(name=str(row['Họ và Tên']),
                                              birth=str(
                                                  row['Ngày/Tháng/Năm sinh']),
                                              date_enter_company=str(
                                                  row['Ngày bắt đầu làm việc']),
                                              position=int(row['Chức vụ']),
                                              status=int(row['Vị trí']),
                                              expected_work_day=int(
                                                  row['Tổng số ngày công']),
                                              day_off=int(row['Nghỉ phép']),
                                              bank=str(row['Tài khoản']),
                                              bank_name=str(row['Ngân hàng'])
                                              ))
            elif int(row['Chức vụ']) == 5:
                employees.append(Janitor(name=str(row['Họ và Tên']),
                                         birth=str(row['Ngày/Tháng/Năm sinh']),
                                         date_enter_company=str(
                                             row['Ngày bắt đầu làm việc']),
                                         position=int(row['Chức vụ']),
                                         status=int(row['Vị trí']),
                                         expected_work_day=int(
                                             row['Tổng số ngày công']),
                                         day_off=int(row['Nghỉ phép']),
                                         bank=str(row['Tài khoản']),
                                         bank_name=str(row['Ngân hàng'])
                                         ))
            elif int(row['Chức vụ']) == 6:
                employees.append(Security(name=str(row['Họ và Tên']),
                                          birth=str(row['Ngày/Tháng/Năm sinh']),
                                          date_enter_company=str(
                                              row['Ngày bắt đầu làm việc']),
                                          position=int(row['Chức vụ']),
                                          status=int(row['Vị trí']),
                                          expected_work_day=int(
                                              row['Tổng số ngày công']),
                                          day_off=int(row['Nghỉ phép']),
                                          bank=str(row['Tài khoản']),
                                          bank_name=str(row['Ngân hàng'])
                                          ))

    return employees


# sale_logic = get_sale_logic_file()
# print(sale_logic)

# pt_logic = get_pt_logic_file()
# print(pt_logic)

# ef = create_employee_list()
# for i in range(len(ef)):
#    print(ef[i])

a = get_actual_day_of_work()
print(a)

# a = get_salary_report()
# print(a)

a = create_employee_list()
for i in range(len(a)):
    if a[i].position == 3:
        print(a[i])
        b = a[i].get_total_salary()
        print(a[i].name + ' = ' + str(b))
    # print(a[i])
    # if a[i].position == 2:
    #    b = a[i].get_total_salary()
    #    print(a[i].name + ' = ' + str(b))
