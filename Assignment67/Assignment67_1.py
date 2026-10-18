#----------------------------------------------------------------------------
# Customer Churn Prediction using FNN
#----------------------------------------------------------------------------
# 1. Load or Create Dataset
# 2. Clean the Dataset
# 3. Feature Scaling (StandardScaler)
# 4. FNN Model Training
# 5. Model Evaluation
# 6. Test Unseen Data
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
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
]

Y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

data = pd.DataFrame(X, columns=[
    'Age', 'MonthlyCharges', 'Tenure',
    'Complaints', 'SupportCalls'
])

data['Churn'] = Y

print("Complete Dataset:")
print(data)

#----------------------------------------------------------------------------
# 2. Clean the Dataset
#----------------------------------------------------------------------------
print(border)
print("2. Clean the Dataset")
print(border)

print("Missing Values:")
print(data.isnull().sum())

data = data.drop_duplicates()
data = data.dropna()

X = data[['Age', 'MonthlyCharges', 'Tenure',
          'Complaints', 'SupportCalls']]

Y = data['Churn']

print("Cleaned Dataset:")
print(data)

#----------------------------------------------------------------------------
# 3. Feature Scaling (StandardScaler)
#----------------------------------------------------------------------------
print(border)
print("3. Feature Scaling (StandardScaler)")
print(border)

scalar = StandardScaler()

X_scaled = scalar.fit_transform(X)

print("Scaled Input Data:")
print(X_scaled)

#----------------------------------------------------------------------------
# 4. FNN Model Training
#----------------------------------------------------------------------------
print(border)
print("4. FNN Model Training")
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
# 5. Model Evaluation
#----------------------------------------------------------------------------
print(border)
print("5. Model Evaluation")
print(border)

Y_pred = model.predict(X_scaled)

accuracy = accuracy_score(Y, Y_pred)

print("Accuracy is:", accuracy)

#----------------------------------------------------------------------------
# 6. Test Unseen Data
#----------------------------------------------------------------------------
print(border)
print("6. Test Unseen Data")
print(border)

new_customer = pd.DataFrame(
    [[46, 1450, 5, 6, 9]],
    columns=[
        'Age', 'MonthlyCharges', 'Tenure',
        'Complaints', 'SupportCalls'
    ]
)

new_customer_scaled = scalar.transform(new_customer)

new_prediction = model.predict(new_customer_scaled)

print("New Customer Data:")
print(new_customer)

if new_prediction[0] == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")