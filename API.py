from fastapi import FastAPI
import mysql.connector
import pandas as pd

db= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='companyshares'
)

mycursor=db.cursor()
app=FastAPI()

import time
import datetime
import pandas as pd

tickers = ['TSLA']
interval = '1d'
period1 = int(time.mktime(datetime.datetime(2021, 1, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 6, 30, 23, 59).timetuple()))

xlwriter = pd.ExcelWriter('historical prices.xlsx', engine='openpyxl')
for ticker in tickers:
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    df = pd.read_csv(query_string)
    df.to_excel(xlwriter, sheet_name=ticker, index=False)

xlwriter.save()