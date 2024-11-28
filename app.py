from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Heart Disease Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON data
        data = request.get_json()

        # Extract features
        features = data['features']  # Expecting a list of 13 features
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features).max()

        # Return prediction
        result = {
            'prediction': int(prediction),  # 0: No heart disease, 1: Heart disease
            'probability': round(probability, 2)
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
