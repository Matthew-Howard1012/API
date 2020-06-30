
import pandas as pd
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api  

# creating a Flask app 
app = Flask(__name__) 
api = Api(app)

#Read file
data = pd.read_excel (r'C:\Users\a058986\Documents\test_data.xlsx') 
data_dict = data.to_dict()
print (data_dict) 
           

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return (data_dict)



  
# driver function 
if __name__ == '__main__': 
  
    app.run()
