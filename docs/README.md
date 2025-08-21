# Telco Customer Churn Predictor

A machine learning application that predicts customer churn for a telecommunications company. The application uses a Logistic Regression model trained on historical customer data to predict whether a customer is likely to churn.

## Features

- Machine learning model trained on Telco customer data
- RESTful API built with Flask
- User-friendly web interface
- Real-time churn predictions
- Probability scores for predictions

## Project Structure

```
├── backend/
│   └── churn_predictor.py    # Flask API server
├── frontend/
│   ├── index.html           # Web interface
│   └── styles.css           # Styling
├── train_model.py           # Model training script
├── Telco_Churn.csv          # Dataset
├── model.pkl               # Trained model
├── label_encoders.pkl      # Categorical encoders
├── scaler.pkl             # Feature scaler
└── requirements.txt        # Python dependencies
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Pratt33/teleco-churn-prediction
cd telco-churn-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Train the model):
```bash
python train_model.py
```

## Running the Application

The application requires two servers to run: a Flask backend and a Python HTTP server for the frontend.

### 1. Start the Flask Backend

Open a terminal and run:
```bash
cd backend
python churn_predictor.py
```

### 2. Start the Frontend Server

Open a new terminal and run:
```bash
cd frontend
python -m http.server 8000
```


## API Usage

The prediction API endpoint accepts POST requests with customer data:

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 24,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}'
```

## Model Details

- Algorithm: Logistic Regression
- Features: 19 customer attributes
- Target: Binary classification (Churn: Yes/No)


## License

This project is licensed under the MIT License - see the LICENSE file for details.
