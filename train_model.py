import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('Telco_Churn.csv')

# Drop customerID as it's not useful for prediction
df = df.drop('customerID', axis=1)

# Convert TotalCharges to numeric, handling any non-numeric values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())

# Identify categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns

# Create a dictionary to store label encoders
label_encoders = {}

# Encode categorical variables
print("Encoding categorical variables...")
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Save the label encoders for future use
joblib.dump(label_encoders, 'label_encoders.pkl')

# Prepare features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler for future use
joblib.dump(scaler, 'scaler.pkl')

# Train the model
print("Training logistic regression model...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Print model performance
print("\nModel Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the model
print("\nSaving model...")
joblib.dump(model, 'model.pkl')
print("Model saved as 'model.pkl'") 