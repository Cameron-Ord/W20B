import mariadb
import dbcreds
import json
from flask import Flask

app = Flask(__name__)
#establishing connection

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

def end_conn():
    if(cursor !=None):
        cursor.close()
    if(conn !=None):
        conn.close()

#closes conn and cursor

@app.get('/dogs')
def select_dogs():
    cursor.execute('CALL select_dogs()')
    results = cursor.fetchall()
#json stringifies results
    if(type(results) == list):
        rst_json = json.dumps(results, default=str)
        end_conn()
        return rst_json
    else:
        print("error")
        end_conn()

@app.get('/cats')
def select_cats():
    #calls the proceedure
    cursor.execute('CALL select_cats()')
    results = cursor.fetchall()
#json stringifies results
    if(type(results) == list):
        rst_json = json.dumps(results, default=str)
        end_conn()
        return rst_json
    else:
        print("error")
        end_conn()

@app.get('/animals')
def get_animals():
    #calls the proceedure
    cursor.execute('CALL select_animals()')
    results = cursor.fetchall()
#json stringifies results
    if(type(results) == list):
        rst_json = json.dumps(results, default=str)
        end_conn()
        return rst_json
    else:
        print("error")
        end_conn()


app.run(debug=True)