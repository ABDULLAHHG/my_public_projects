from flask import Flask , request
import pandas as pd 
import requests  

df = pd.read_csv('mobile_recommendation_system_dataset.csv')
app = Flask(__name__)
names = df.name.unique()
names = [str.replace(i,"'",'"') for i in names]
@app.route("/names")
def hello_world():
    return {"names" : names}


@app.route('/save_selected_value', methods=['POST'])
def save_selected_value():
    selected_value = request.json['selectedValue']
    # do something with selected_value, such as store it in a database or file
    return ''

if __name__ == "__main__":
    app.run(debug=True)
