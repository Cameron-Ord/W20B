import mariadb
import dbcreds
import json
from flask import Flask
import dbhelper

app = Flask(__name__)


conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

@app.get('/dogs')
def select_dogs():
   results = dbhelper.run_proceedure('CALL select_dogs', [])
   results_json = json.dumps(results, default=str)
   return results_json

@app.get('/cats')
def select_cats():
   results = dbhelper.run_proceedure('CALL select_cats', [])
   results_json = json.dumps(results, default=str)
   return results_json

@app.get('/animals')
def get_animals():
   results = dbhelper.run_proceedure('CALL select_animals', [])
   results_json = json.dumps(results, default=str)
   return results_json


app.run(debug=True)