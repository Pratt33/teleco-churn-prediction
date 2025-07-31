from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get the parent directory path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the saved model and preprocessing components with correct paths
model = joblib.load(os.path.join(parent_dir, 'model.pkl'))
label_encoders = joblib.load(os.path.join(parent_dir, 'label_encoders.pkl'))
scaler = joblib.load(os.path.join(parent_dir, 'scaler.pkl'))

# Define the expected features in order
expected_features = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
    'MonthlyCharges', 'TotalCharges'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Create a DataFrame with a single row, ensuring correct feature order
        input_df = pd.DataFrame([{feature: data.get(feature, 'No') for feature in expected_features}])
        
        # Convert TotalCharges to numeric
        input_df['TotalCharges'] = pd.to_numeric(input_df['TotalCharges'], errors='coerce')
        input_df['TotalCharges'] = input_df['TotalCharges'].fillna(input_df['TotalCharges'].mean())
        
        # Encode categorical variables
        for column in label_encoders.keys():
            if column in input_df.columns:
                input_df[column] = label_encoders[column].transform(input_df[column])
        
        # Scale the features
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Convert prediction to "Yes" or "No"
        churn_prediction = "Yes" if prediction == 1 else "No"
        
        return jsonify({
            'churn_prediction': churn_prediction,
            'probability': float(model.predict_proba(input_scaled)[0][1])
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 