from flask import Flask, request, jsonify
from flasgger import Swagger
import os
import pickle
import pandas as pd

app = Flask(__name__)
swagger = Swagger(app)

filename = os.path.join("model","linear_regression_model.pkl")
with open(filename, 'rb') as model_file:
    pipeline = pickle.load(model_file)

@app.route("/predict", methods = ['POST'])
def predict():
    try:
        data = request.get_json()
        new_data = pd.DataFrame(data, index=[0])
        new_data = new_data.values.reshape(-1, 1)
        prediction = pipeline.predict(new_data)
        return jsonify({"prediction": prediction[0]})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)