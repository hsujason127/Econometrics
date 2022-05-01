import os
import pandas as pd
import time
import random

def twse_crawler():
    start_year = int(input('請輸入起始年份：'))
    end_year = int(input('請輸入結束年份：'))

    ## curren working directory
    cwd = os.getcwd()
    cwd
    
    def normalize_date(char):
        if len(char) == 1:
            char = '0' + char
        else:
            char = char
        return char
    
    ## define the function
    def get_data(yymmdd):
        ## set the url
        url = f'https://www.twse.com.tw/fund/BFI82U?response=html&dayDate=' + yymmdd
        ## save the results into dataframe
        raw = pd.read_html(url, encoding='utf-8',header=0)[0]

        ## get the amount
        table = raw.iloc[1:6, 3].tolist()
        return table    

    ## Set the query
    years = [str(year) for year in range(start_year, end_year+1)]
    months = [normalize_date(str(month)) for month in range(1, 13)]
    dates = [normalize_date(str(day)) for day in range(1, 32)]

    ## create an empty list
    data = []

    ## create a query list
    alldates = []
    for year in range(len(years)):
        for month in range(len(months)):
            for date in range(len(dates)):
                alldates.append(years[year] + months[month] + dates[date])

    row = 1
    for i in range(0, len(alldates)):
        time.sleep(2)
        try:
            data.append([alldates[i]] + get_data(alldates[i]))
            print([alldates[i]] + get_data(alldates[i]))
            time.sleep(2)
        except ValueError:
            print(f"很抱歉，沒有符合 {alldates[i]} 的資料")
            time.sleep(2)

    data_sets = pd.DataFrame(data)
    data_sets.columns = ['年份', '自營商(自行買賣)', '自營商(避險)', '投信', '外資及陸資(不含外資自營商)', '外資自營商']
    data_sets.to_csv(cwd + 'twse_data.csv', encoding='utf-8-sig')
    return data_sets

twse_crawler()