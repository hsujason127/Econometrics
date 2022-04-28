import pandas as pd
import time

def get_data(yymmdd):
    ## set the url
    url = f'https://www.twse.com.tw/fund/BFI82U?response=html&dayDate=' + yymmdd
    ## save the results into dataframe
    raw = pd.read_html(url, encoding='utf-8',header=0)[0]

    ## get the amount
    amount = raw.iloc[1:5, 3].tolist()
    return amount    

## Set the query
years = ['2017', '2018', '2019', '2020', '2021']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
dates = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

## valueError

## create an empty list
row = 1
data = []

## create a query list
alldates = []
for year in range(len(years)):
    for month in range(len(months)):
        for date in range(len(dates)):
            alldates.append(years[year] + months[month] + dates[date])

for i in range(0, len(alldates)):
    time.sleep(3)
    try:
        data.append([alldates[i]] + get_data(alldates[i]))
    except ValueError:
        print(f"There is no data in {alldates[i]}")

data_sets = pd.DataFrame(data)
data_sets.to_excel('twse_data.xlsx')