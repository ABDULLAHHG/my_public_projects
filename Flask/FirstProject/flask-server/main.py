from flask import Flask , request , jsonify
import pandas as pd 

df = pd.read_csv('mobile_recommendation_system_dataset.csv')

app = Flask(__name__)
df =df.sort_values('name')

names = df.name.unique()
names = [str.replace(i,"'",'"') for i in names]
@app.route("/names")
def hello_world():
    return {"names" : names}


@app.route('/save_selected_value', methods=['POST'])
def save_selected_value():
    selected_value = request.json['selectedValue']
    url = "".join(df[df.name == selected_value].imgURL.astype(str).values)
    price = "".join(df[df.name == selected_value].price.astype(str).values)
    ratings = "".join(df[df.name == selected_value].ratings.astype(str).values)
    corpus = "".join(df[df.name == selected_value].corpus.astype(str).values)
    print(url)
    print(price)
    print(ratings)
    print(corpus)

    return({"URL" : url ,
            "Price":price,
            "Ratings":ratings,
            "Corpus":corpus})

if __name__ == "__main__":
    app.run(debug=True)
