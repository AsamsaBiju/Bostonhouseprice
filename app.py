from flask import Flask, render_template, request
import pickle
import numpy as np

print("👉 Flask app is starting...")  # Add this line

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    prediction = model.predict([input_features])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'Estimated House Price: ${output}')

if __name__ == '__main__':
    print("✅ app.py is running")  # Add this line
    app.run(debug=True)