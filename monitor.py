from __future__ import annotations
from openpyxl import load_workbook
import pandas as pd
from typing import List


def split_list(lst, n):
    """Split a list into sublists containing n elements."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def get_actual_day_of_work() -> dict:
    """
    Read the file then calculate the actual day of work for each employee
    Return the actual total day of work for each employee in dictionary data
    type

    :return: dict
    """
    dw_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx',
                            sheet_name='C.C')
    dw_f = pd.DataFrame(dw_file, columns=['Tên NV', 'Ngày công'])
    cc = {}

    for index, row in dw_f.iterrows():
        if str(row['Tên NV']).lower() != 'nan':
            if row['Tên NV'] not in cc.keys():
                cc[row['Tên NV']] = round(float(row['Ngày công']), 2)
            else:
                cc[row['Tên NV']] += round(float(row['Ngày công']), 2)

    return cc


def get_performance_report() -> dict:
    """
    Read the salary report of the month file to calculate how much each
    sale and each pt made for the month

    :return: dict
    """
    salary_file = pd.read_excel('input-file/Bao-cao-CD-thang-02-2023.xlsx',
                                sheet_name='PS')
    sa_f = pd.DataFrame(salary_file, columns=['Sale', 'VIP', 'GYM', 'PT/KB'])
    # print(sa_f)
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
                report[str(row['Sale'])] = vip + gym + pt
            else:
                report[str(row['Sale'])] += vip + gym + pt

    return report
