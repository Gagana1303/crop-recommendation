import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd 

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    input_data = {
        "temperature": float(request.form['temperature']),
        "N": float(request.form['nitrogen']),
        "P": float(request.form['phosphorus']),
        "K": float(request.form['potassium']),
        "humidity": float(request.form['humidity']),
        "ph": float(request.form['ph']),
        "rainfall": float(request.form['rainfall'])
    }

    df = pd.DataFrame([input_data])
    df = df[model.feature_names_in_]

    prediction = model.predict(df)[0]

    return render_template('index.html', prediction=prediction)


if __name__ == "__main__":
    app.run()
