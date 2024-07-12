import csv
from datetime import datetime

def UserDataParsing(file, option, header, data):


    if option == 1:
        data_by_date = {}
        for col in file:
            date = datetime.strptime(col[f'{header}'], '%m/%d/%Y')

            date_str = date.strftime('%m/%d/%Y')
            data_ = int(col[f'{data}'])

            if date_str in data_by_date:
                data_by_date[date_str] += data_
            else:
                data_by_date[date_str] = data_
        print("Accumulated Data By Date:", data_by_date)

    elif option == 2:
        data_by_set = {}
        for col in file:
            setData = col[header]
            data_ = int(col[data])

            if setData in data_by_set:
                data_by_set[setData] += data_
            else:
                data_by_set[setData] = data_
        print("Accumulated Data By Set:", data_by_set)



def UserOptions():
    print('1: Return Accumulated Data By Date')
    print('2: Return Accumulated Data By Set')
    print('3: Sort Data By Set and Sum = ex. Country and Sum of Sales/Data')
    print('4: Sort Data By Sets - ex. Country and Date and Sum of Data related to Country')


with open('report2.csv', 'r', encoding='utf-8-sig') as filename:
    file = csv.DictReader(filename)

    headers = file.fieldnames

    print(f'Current Headers: {headers}')

    UserDataParsing(file, 2, 'Marketplace', 'Sold')




    """""
    for col in file:
        try:
            date = datetime.strptime(col['Dates Sold'], '%m/%d/%Y')
            dates.append(date)
        except ValueError as e:
            print(f'Error parsing date in row {col}')
            print(e)
        except KeyError as e:
            print(f'Mssing column in row: {col}')
            print(e)


    print('Dates: ', dates)
    """""
