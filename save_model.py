import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# Load dataset
heart_data = pd.read_csv('data.csv')
X = heart_data.drop(columns='target')
Y = heart_data['target']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
param_grid = {'C': [0.01, 0.1, 1, 10, 100], 'solver': ['lbfgs', 'liblinear']}
model = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5)
model.fit(X_scaled, Y)

# Save the model and scaler to .pkl files
joblib.dump(model, 'heart_disease_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
