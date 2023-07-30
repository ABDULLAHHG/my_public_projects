from flask import Flask
import pandas as pd 

df = pd.read_csv('mobile_recommendation_system_dataset.csv')
app = Flask(__name__)
names = df.name.unique()
names = [str.replace(i,"'",'"') for i in names]
@app.route("/names")
def hello_world():
    return {"names" : names}

if __name__ == "__main__":
    app.run(debug=True)