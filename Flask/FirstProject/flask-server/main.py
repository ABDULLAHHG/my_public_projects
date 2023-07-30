from flask import Flask , request , jsonify
import pandas as pd 

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
    url = ''.join(list(df[df.name == selected_value].imgURL))
    return {'URL' : url}

if __name__ == "__main__":
    app.run(debug=True)
