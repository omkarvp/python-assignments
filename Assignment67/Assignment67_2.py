#----------------------------------------------------------------------------
# Loan Approval Prediction using FNN
#----------------------------------------------------------------------------
# 1. Load or Create Dataset
# 2. Preprocessing Categorical Values
# 3. Clean the Dataset
# 4. Feature Scaling (StandardScaler)
# 5. FNN Model Training
# 6. Model Evaluation
# 7. Test Unseen Data
#----------------------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

border = "-" * 65

#----------------------------------------------------------------------------
# 1. Load or Create Dataset
#----------------------------------------------------------------------------
print(border)
print("1. Load or Create Dataset")
print(border)

X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
]

Y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

data = pd.DataFrame(X, columns=[
    'Income', 'CreditScore', 'LoanAmount',
    'ExistingEMI', 'EmploymentStatus'
])

data['LoanApproval'] = Y

print("Complete Dataset:")
print(data)

#----------------------------------------------------------------------------
# 2. Preprocessing Categorical Values
#----------------------------------------------------------------------------
print(border)
print("2. Preprocessing Categorical Values")
print(border)

data['EmploymentStatus'] = data['EmploymentStatus'].map({
    0: 0,
    1: 1
})

print("Categorical Values Converted:")
print(data['EmploymentStatus'])

#----------------------------------------------------------------------------
# 3. Clean the Dataset
#----------------------------------------------------------------------------
print(border)
print("3. Clean the Dataset")
print(border)

print("Missing Values:")
print(data.isnull().sum())

data = data.drop_duplicates()
data = data.dropna()

X = data[['Income', 'CreditScore', 'LoanAmount',
          'ExistingEMI', 'EmploymentStatus']]

Y = data['LoanApproval']

print("Cleaned Dataset:")
print(data)

#----------------------------------------------------------------------------
# 4. Feature Scaling (StandardScaler)
#----------------------------------------------------------------------------
print(border)
print("4. Feature Scaling (StandardScaler)")
print(border)

scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)

print("Scaled Input Data:")
print(X_scaled)

#----------------------------------------------------------------------------
# 5. FNN Model Training
#----------------------------------------------------------------------------
print(border)
print("5. FNN Model Training")
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    solver="adam",
    max_iter=2000,
    random_state=42
)

print(model)

model.fit(X_scaled, Y)

print("Model trained successfully")

#----------------------------------------------------------------------------
# 6. Model Evaluation
#----------------------------------------------------------------------------
print(border)
print("6. Model Evaluation")
print(border)

Y_pred = model.predict(X_scaled)

accuracy = accuracy_score(Y, Y_pred)

print("Accuracy is:", accuracy)

#----------------------------------------------------------------------------
# 7. Test Unseen Data
#----------------------------------------------------------------------------
print(border)
print("7. Test Unseen Data")
print(border)

new_applicant = pd.DataFrame(
    [[55000, 720, 400000, 10000, 1]],
    columns=[
        'Income', 'CreditScore', 'LoanAmount',
        'ExistingEMI', 'EmploymentStatus'
    ]
)

new_applicant_scaled = scalar.transform(new_applicant)

new_prediction = model.predict(new_applicant_scaled)

print("New Applicant Data:")
print(new_applicant)

if new_prediction[0] == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")