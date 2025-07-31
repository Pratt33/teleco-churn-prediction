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
git clone <repository-url>
cd telco-churn-predictor
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Train the model (if not using pre-trained model):
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
The backend server will start at http://localhost:5000

### 2. Start the Frontend Server

Open a new terminal and run:
```bash
cd frontend
python -m http.server 8000
```
The frontend server will start at http://localhost:8000

### 3. Access the Application

Open your web browser and navigate to:
```
http://localhost:8000
```

Note: Both servers must be running simultaneously for the application to work properly.

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

## Troubleshooting

1. If you get a "No such file or directory" error:
   - Make sure you're in the correct directory
   - Verify that all files are in their proper locations
   - Check that the model files (model.pkl, label_encoders.pkl, scaler.pkl) exist

2. If the frontend can't connect to the backend:
   - Ensure both servers are running
   - Check that you're using the correct URLs
   - Verify that no other applications are using ports 5000 or 8000

## Model Details

- Algorithm: Logistic Regression
- Features: 19 customer attributes
- Target: Binary classification (Churn: Yes/No)
- Performance metrics available in model training output

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset: Telco Customer Churn Dataset
- Built with Flask and scikit-learn