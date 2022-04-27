import pandas as pd
import time

## Set the query
years = ['2017', '2018', '2019', '2020', '2021']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
dates = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

## valueError

## create an empty dataframe
row = 1
data = pd.DataFrame(columns=['yy-mm-dd', '自營商(自行買賣)', '自營商(避險)', '投信', '外資及陸資'])

for year in range(len(years)):
    for month in range(len(months)):
        for date in range(len(dates)):
            yymmdd = years[year] + months[month] + dates[date]
            try:
                data.loc[row] = get_data(yymmdd)
                print(get_data(yymmdd))
                row += 1
                time.sleep(5)
            except ValueError:
                print(f"error occured in {years[year]+months[month]+dates[date]}")
                time.sleep(5)