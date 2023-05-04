import pandas

excel_file = 'logic-file/pt-logic.xlsx'

df = pandas.read_excel(excel_file, None)


if __name__ == '__main__':
    print(df)
