# K-Nearest Neighbors on diabetes.csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# 1. LOAD
df = pd.read_csv("diabetes.csv")
print(df.head())

# 2. CLEAN: 0 is impossible in these columns, so treat it as missing
#    and fill it with the column median
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for c in cols:
    df[c] = df[c].replace(0, df[c].median())

# 3. X and y (Outcome: 1 = diabetic, 0 = not diabetic)
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# 4. SPLIT and SCALE (KNN uses distance, so scaling is important)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. MODEL
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

# 6. EVALUATE
acc = accuracy_score(y_test, pred)
print("\nConfusion Matrix:\n", confusion_matrix(y_test, pred))
print("Accuracy   :", acc)
print("Error rate :", 1 - acc)
print("Precision  :", precision_score(y_test, pred))
print("Recall     :", recall_score(y_test, pred))

# -----------------------------------------
# SAMPLE INPUT:
# Dataset: diabetes.csv
#
# SAMPLE OUTPUT:
# Confusion Matrix:
# [[... ...]
#  [... ...]]
# Accuracy: (Calculated value)
# Error Rate: (Calculated value)
# Precision: (Calculated value)
# Recall: (Calculated value)
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P9.py
# -----------------------------------------
