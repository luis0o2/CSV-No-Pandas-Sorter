import csv
from datetime import datetime

def UserDataParsing(file, option, header, data):


    if option == '1':
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

    elif option == '2':
        data_by_set = {}
        for col in file:
            setData = col[header]
            data_ = int(col[data])

            if setData in data_by_set:
                data_by_set[setData] += data_
            else:
                data_by_set[setData] = data_
        return data_by_set

    elif option == '3':
        datas_by_set = {}
        header2 = str(input('Enter Header 2: '))
        for col in file:
            data1 = col[header]
            data2 = col[header2]
            data3 = int(col[data])

            if data1 not in datas_by_set:
                datas_by_set[data1] = {}

            if data2 in datas_by_set[data1]:
                datas_by_set[data1][data2] += data3
            else:
                datas_by_set[data1][data2] = data3

        return datas_by_set

    elif option == '4':
        data_sum = {}
        data_count = {}

        for col in file:
            data1 = col[header]
            data2 = int(col[data])

            if data1 not in data_sum:
                data_sum[data1] = 0
                data_count[data1] = 0

            data_sum[data1] += data2
            data_count[data1] += 1

        average = {data1: data_sum[data1] / data_count[data1] for data1 in data_sum}
        return average










def UserOptions():
    print('1: Return Accumulated Data By Date')
    print('2: Return Accumulated Data(1) By Set')
    print('3: Return Accumulated Datas(2) By Set')
    print('4: Return Average of Data By Set')
    print('5: Quit')


with open('report.csv', 'r', encoding='utf-8-sig') as filename:
    file = csv.DictReader(filename)
    headers = file.fieldnames
    data = list(file)





    while True:
        UserOptions()
        choice = input('Choose one of these options: ')
        if choice == '5':
            print("Exiting program.")
            break
        print('Current Headers:')
        for header in headers:
            print(header)
        data1 = input('Give me a header(Date, data, etc): ')
        data2 = input('Give me data: ')

        show = UserDataParsing(data, choice, f'{data1}', f'{data2}')
        print(show)



