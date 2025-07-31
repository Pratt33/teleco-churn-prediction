import pandas as pd

# Load raw data
df = pd.read_csv('data/Telco_Churn.csv')

# Example preprocessing: drop missing values
df = df.dropna()

# Save processed data
df.to_csv('data/processed.csv', index=False)