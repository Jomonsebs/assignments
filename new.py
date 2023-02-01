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

@app.get("/")
def root():
    return "TSWORKS"

@app.get("/day-shares")
def endpoint(s_date):
    req="SELECT * FROM share_log where Date="+"'"+s_date+"';"
    mycursor.execute(req)
    return "Success"

@app.get("/company-per-day")
def endpoint(comp,s_date):
    req="SELECT * FROM share_log where Date='"+ s_date+"'"+ "and comp_name='"+comp+"';"
    mycursor.execute(req)
    return "Success"

@app.get("/stock/company-share")
def endpoint(comp):
    req="SELECT * FROM share_log where comp_name='"+str(comp)+"';"
    mycursor.execute(req)
    return "Success"

@app.post("/stock/update")
def endpoint(comp,s_date,op):
    req="UPDATE share_log SET="+str(op)+ " WHERE comp_name='" +comp+ "' and Date='"+s_date+ "';"
    mycursor.execute(req)
    return "Update Success"

companies=list()
@app.post("/stock/download")
def endpoint():
    f= open("config.txt",'r')
    for line in f:
        companies.append(line.rstrip())
    f.close()
    return companies


