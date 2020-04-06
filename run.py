from flask import Flask
import pymssql
import pandas as pd

server = '192.168.4.117'
database = 'FreedomCashLenders'
username = 'FreedomCashLendersAll'
mssql_password = 'Freedom123$'
mysql_password = 'FreedomML123$'

conn = pymssql.connect(server,username,mssql_password,database,port=1433)

df_sample = pd.read_sql_query('SELECT TOP 1 LoanId FROM view_FCL_Loan',con=conn)

app = Flask(__name__)



@app.route('/')
def test():
    return {'message':df_sample.shape}

@app.route('/test')
def test2():
    return {'message':'deployed to ebs using codepipeline'}


if __name__ == "__main__":
    app.run(host='0.0.0.0')