# Bank Customer Churn Prediction using Neural Network
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# ---------- 1. Read the dataset ----------
df = pd.read_csv("Churn_Modelling.csv")
print(df.head())

# ---------- 2. Features, target, train/test split ----------
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)          # not useful
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)  # text -> numbers

X = df.drop("Exited", axis=1).astype(float)    # Exited: 1 = left, 0 = stayed
y = df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# ---------- 3. Normalize ----------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # learn from train data only
X_test = scaler.transform(X_test)

# ---------- 4. Build the model ----------
# Model 1: simple network (1 hidden layer)
model1 = MLPClassifier(hidden_layer_sizes=(6,), max_iter=200, random_state=1)
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

# Improvement: more layers and neurons + early stopping to avoid overfitting
model2 = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500,
                       early_stopping=True, random_state=1)
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

# ---------- 5. Accuracy and confusion matrix ----------
print("\n===== Model 1 (simple) =====")
print("Accuracy:", accuracy_score(y_test, pred1))
print(confusion_matrix(y_test, pred1))

print("\n===== Model 2 (improved) =====")
print("Accuracy:", accuracy_score(y_test, pred2))
print(confusion_matrix(y_test, pred2))

# ---------- 6. Predict: will a customer leave in the next 6 months? ----------
print("\nPrediction:", "Will LEAVE" if model2.predict(X_test[[0]])[0] == 1 else "Will STAY",
      "| Actual:", "Left" if y_test.iloc[0] == 1 else "Stayed")



# -----------------------------------------
# SAMPLE INPUT:
# Dataset: Churn_Modelling.csv
#
# SAMPLE OUTPUT:
# Accuracy: (Calculated value)
# Confusion Matrix:
# [[... ...]
#  [... ...]]
# Customer prediction: (Stay or Leave)
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P8.py
# -----------------------------------------
