import streamlit as st 
import pandas as pd
import numpy as np

# Number of samples (rows) you want
num_samples = 500  

# Number of feature columns
num_features = 55  

# Generate random feature data
# Values between 0 and 1 for simplicity
X = np.random.rand(num_samples, num_features)

# Generate random labels: 'malicious' or 'benign'
labels = np.random.choice(['malicious', 'benign'], size=num_samples)

# Create column names f1, f2, ..., f55
feature_columns = [f"f{i}" for i in range(1, num_features + 1)]

# Build DataFrame
df = pd.DataFrame(X, columns=feature_columns)
df['label'] = labels

# Save to CSV
df.to_csv("malware_features.csv", index=False)

print("CSV file 'malware_features.csv' created with", num_samples, "rows and", num_features, "feature columns.")
