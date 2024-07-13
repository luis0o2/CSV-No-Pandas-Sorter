import csv
import matplotlib.pyplot as plt

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

        sorted_data_by_date = dict(sorted(data_by_date.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y')))
        return sorted_data_by_date

    elif option == 2:
        data_by_set = {}
        for col in file:
            setData = col[header]
            data_ = int(col[data])

            if setData in data_by_set:
                data_by_set[setData] += data_
            else:
                data_by_set[setData] = data_
        return data_by_set



def UserOptions():
    print('1: Return Accumulated Data By Date')
    print('2: Return Accumulated Data By Set')
    print('3: Sort Data By Set and Sum = ex. Country and Sum of Sales/Data')
    print('4: Sort Data By Sets - ex. Country and Date and Sum of Data related to Country')


with open('report2.csv', 'r', encoding='utf-8-sig') as filename:
    file = csv.DictReader(filename)
    data = list(file)

    headers = file.fieldnames

    print(f'Current Headers: {headers}')

    CountrySales = UserDataParsing(data, 2, 'Marketplace', 'Sold')

    plt.bar(CountrySales.keys(), CountrySales.values(), 1.0, color='b')
    plt.show()

    TimeSales = UserDataParsing(data, 1, 'Date', 'Sold')


    plt.bar(TimeSales.keys(), TimeSales.values(), 1.0, color='g')
    plt.show()



