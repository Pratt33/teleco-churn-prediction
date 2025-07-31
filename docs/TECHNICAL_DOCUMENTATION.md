# Telco Churn Predictor - Technical Documentation

## 1. System Architecture

### 1.1 Overview
The application follows a client-server architecture with three main components:
- Machine Learning Model (Python)
- Backend API (Flask)
- Frontend Interface (HTML/CSS/JavaScript)

### 1.2 Component Interaction
```
[User] → [Frontend (port 8000)] → [Backend API (port 5000)] → [ML Model] → [Response]
```

## 2. Machine Learning Implementation

### 2.1 Data Processing (`train_model.py`)
```python
# Key preprocessing steps:
1. Load Telco_Churn.csv
2. Handle missing values:
   - Convert TotalCharges to numeric
   - Fill missing values with mean
3. Encode categorical variables:
   - Use LabelEncoder for each categorical column
   - Save encoders for future use
4. Scale numerical features:
   - Use StandardScaler
   - Save scaler for future use
```

### 2.2 Model Training
- Algorithm: Logistic Regression
- Features: 19 customer attributes
- Target: Binary classification (Churn: Yes/No)
- Performance metrics: Accuracy and probability scores

### 2.3 Saved Components
- `model.pkl`: Trained Logistic Regression model
- `label_encoders.pkl`: Dictionary of LabelEncoders for categorical variables
- `scaler.pkl`: StandardScaler for numerical features

## 3. Backend Implementation (`backend/churn_predictor.py`)

### 3.1 API Endpoints
```python
POST /predict
- Accepts: JSON with customer details
- Returns: Prediction and probability
```

### 3.2 Request Processing
1. Receive customer data
2. Create DataFrame with correct feature order
3. Apply preprocessing:
   - Encode categorical variables
   - Scale numerical features
4. Make prediction
5. Return result

### 3.3 Error Handling
- Input validation
- Missing feature handling
- Exception handling with appropriate error messages

## 4. Frontend Implementation

### 4.1 User Interface (`frontend/index.html`)
- Form for customer details
- Real-time validation
- Responsive design
- Clear result display

### 4.2 Styling (`frontend/styles.css`)
- Modern, clean design
- Color-coded results
- Responsive layout
- User-friendly form elements

### 4.3 JavaScript Functionality
```javascript
// Key functions:
1. Form data collection
2. API communication
3. Result display
4. Error handling
```

## 5. Data Flow

### 5.1 Training Flow
```
[Raw Data] → [Preprocessing] → [Model Training] → [Save Components]
```

### 5.2 Prediction Flow
```
[User Input] → [Frontend] → [API] → [Preprocessing] → [Prediction] → [Response]
```

## 6. Feature Engineering

### 6.1 Categorical Features
- gender
- SeniorCitizen
- Partner
- Dependents
- PhoneService
- MultipleLines
- InternetService
- Contract
- PaperlessBilling
- PaymentMethod

### 6.2 Numerical Features
- tenure
- MonthlyCharges
- TotalCharges

### 6.3 Additional Services
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies

## 7. Technical Requirements

### 7.1 Python Packages
```
flask==3.0.2
flask-cors==4.0.0
pandas==2.2.3
scikit-learn==1.6.1
joblib==1.4.2
numpy==2.2.4
```

### 7.2 System Requirements
- Python 3.x
- Web browser with JavaScript enabled
- Ports 5000 and 8000 available

## 8. Security Considerations

### 8.1 Current Implementation
- CORS enabled for development
- Input validation
- Error handling

### 8.2 Recommended Improvements
- Add authentication
- Implement rate limiting
- Use HTTPS
- Add input sanitization
- Implement logging

## 9. Deployment

### 9.1 Development Setup
1. Create virtual environment
2. Install dependencies
3. Train model
4. Start backend server
5. Start frontend server

### 9.2 Production Considerations
- Use production WSGI server
- Implement proper security measures
- Set up monitoring
- Configure logging
- Use environment variables

## 10. Future Improvements

### 10.1 Technical Improvements
- Add model retraining pipeline
- Implement A/B testing
- Add more features
- Improve error handling
- Add automated testing

### 10.2 Feature Improvements
- Add user authentication
- Implement user sessions
- Add prediction history
- Add data visualization
- Implement batch predictions

## 11. Troubleshooting Guide

### 11.1 Common Issues
1. CORS errors
2. Missing features
3. Model loading errors
4. Port conflicts
5. Data validation errors

### 11.2 Solutions
1. Check CORS configuration
2. Verify feature order
3. Check file paths
4. Ensure ports are available
5. Validate input data

## 12. Performance Considerations

### 12.1 Current Performance
- Real-time predictions
- Single-threaded processing
- In-memory model loading

### 12.2 Optimization Opportunities
- Implement caching
- Add batch processing
- Use async processing
- Implement load balancing
- Add database integration 