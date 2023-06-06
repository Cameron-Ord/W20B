#importing
import json
from flask import Flask
import dbhelper

app = Flask(__name__)

@app.get('/dogs')
def select_dogs():
   #function that returns the results from run_proceedure when using respective arguments as JSON
   results = dbhelper.run_proceedure('CALL select_dogs', [])
   results_json = json.dumps(results, default=str)
   return results_json

@app.get('/cats')
#function that returns the results from run_proceedure when using respective arguments as JSON
def select_cats():
   results = dbhelper.run_proceedure('CALL select_cats', [])
   results_json = json.dumps(results, default=str)
   return results_json

@app.get('/animals')
def get_animals():
   #function that returns the results from run_proceedure when using respective arguments as JSON
   results = dbhelper.run_proceedure('CALL select_animals', [])
   results_json = json.dumps(results, default=str)
   return results_json


#running @app
app.run(debug=True)