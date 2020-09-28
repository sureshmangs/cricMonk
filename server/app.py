import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/time')
def get_current_time():
    data = request.args.get('data')
    return {'time': data}

@app.route('/predict',methods=['POST'])
def predict():
    prediction = model.predict()




if __name__ == "__main__":
    app.run(debug=True)