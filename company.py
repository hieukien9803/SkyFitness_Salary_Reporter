from __future__ import annotations

from itertools import islice
import pandas as pd
from typing import List
from employee import Employee


def create_employee_list() -> List[Employee]:
    """
    Read the Employee file give by the company, then create employees based
    on the file given

    Precondition: the file stored at <filename> is in the format specified
    by the company.
    """
    employees = []
    employ_file = pd.read_excel('input-file/employees_file.xlsx', engine='openpyxl')
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
            employees.append(Employee(name=str(row['Họ và Tên']),
                                      birth=str(row['Ngày/Tháng/Năm sinh']),
                                      date_enter_company=str(row['Ngày bắt đầu làm việc']),
                                      position=int(row['Chức vụ']),
                                      status=int(row['Vị trí']),
                                      expected_work_day=int(row['Tổng số ngày công']),
                                      day_off=int(row['Nghỉ phép']),
                                      bank=str(row['Tài khoản']),
                                      bank_name=str(row['Ngân hàng'])
                                      ))

    return employees


def split_list(lst, n):
    """Split a list into sublists containing n elements."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]


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


def get_actual_day_of_work() -> dict:
    """
    Read the file then calculate the actual day of work for each employee
    Return the actual total day of work for each employee in dictionary data
    type

    :return: dict
    """
    dw_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx', sheet_name='C.C')
    dw_f = pd.DataFrame(dw_file, columns=['Tên NV', 'Ngày công'])
    cc = {}

    for index, row in dw_f.iterrows():
        if str(row['Tên NV']).lower() != 'nan':
            if row['Tên NV'] not in cc.keys():
                cc[row['Tên NV']] = round(float(row['Ngày công']), 2)
            else:
                cc[row['Tên NV']] += round(float(row['Ngày công']), 2)

    return cc


def get_salary_report() -> dict:
    """
    Read the salary report of the month file to calculate how much each
    sale and each pt made for the month

    :return: dict
    """
    salary_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx', sheet_name='PS')
    sa_f = pd.DataFrame(salary_file, columns=['Sale', 'VIP', 'GYM', 'PT/KB'])
    print(sa_f)
    report = {}
    for index, row in sa_f.iterrows():
        if str(row['Sale']).lower() != 'nan':
            # check if any column row vip gym pt is 'nan' for salary
            if str(row['VIP']).lower() == 'nan':
                vip = 0
            else:
                vip = float(row['VIP'])
            if str(row['GYM']).lower() == 'nan':
                gym = 0
            else:
                gym = float(row['GYM'])
            if str(row['PT/KB']).lower() == 'nan':
                pt = 0
            else:
                pt = float(row['PT/KB'])
            if row['Sale'] not in report.keys():
                report[row['Sale']] = vip + gym + pt
            else:
                report[row['Sale']] += vip + gym + pt

    return report


def get_pt_report() -> dict:
    """
    Read the pt file report to see how much the pt teaches and how much
    each session cost
    :return: dict
    """
    pt_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx', sheet_name='PT')
    pt_f = pd.DataFrame(pt_file, columns=['Sale', 'VIP', 'GYM', 'PT/KB'])
    print(pt_f)
    report = {}
    return report


# sale_logic = get_sale_logic_file()
# print(sale_logic)

# pt_logic = get_pt_logic_file()
# print(pt_logic)

#ef = create_employee_list()
#for i in range(len(ef)):
#    print(ef[i])

#a = get_actual_day_of_work()
#print(a)

#a = get_salary_report()
#print(a)
