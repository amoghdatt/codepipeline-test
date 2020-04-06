from flask import Flask
import pymssql
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urllib

server = '192.168.4.117'
database = 'FreedomCashLenders'
username = 'FreedomCashLendersAll'
mssql_password = 'Freedom123$'
mysql_password = 'FreedomML123$'

params_iloans = urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'Server='+server+';'+
    'Database='+database+';'+
    'UID='+username+';'+
    'PWD='+mssql_password+';'+
    'TDS_Version=8.0;'+
    'Port=1433;')

#conn = pymssql.connect(server,username,mssql_password,database,port=1433)

#df_sample = pd.read_sql_query('SELECT TOP 1 LoanId FROM view_FCL_Loan',con=conn)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect={}'.format(params_iloans)
db = SQLAlchemy(app)

class GetCreditDataLoan(db.Model):
        __tablename__ = 'view_FCL_GetCreditDataLoan'
        __table_args__ = {'extend_existing': True}

        LoanId = db.Column(db.String,primary_key=True)
        BankTransactionId = db.Column(db.String(100))

gcd = GetCreditDataLoan.query.filter(
    GetCreditDataLoan.BankTransactionId=='ca432336-5028-40d9-81dd-3b9b1b81c6b0'
).first()


@app.route('/')
def test():
    return {'message':str(gcd.LoanId)}

@app.route('/test')
def test2():
    return {'message':gcd.BankTransactionId}

@app.route('/staging')
def test3():
    return {'message':'response from staging'}

@app.route('/production')
def test4():
    return {'message':'response from production'}

if __name__ == "__main__":
    app.run(host='0.0.0.0')