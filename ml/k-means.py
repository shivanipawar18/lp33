# K-Means Clustering on sales_data_sample.csv with Elbow Method
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# read data (file has special characters, so use latin1)
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# choose numeric columns for clustering
cols = ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]
data = df[cols].dropna()

# scale the data so all columns have equal importance
X = StandardScaler().fit_transform(data)

# ---------- Elbow method ----------
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=1, n_init=10)
    km.fit(X)
    inertia.append(km.inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# ---------- Final model (pick k from the elbow, usually 3 or 4) ----------
k = 3
km = KMeans(n_clusters=k, random_state=1, n_init=10)
data = data.copy()
data["Cluster"] = km.fit_predict(X)

print(data["Cluster"].value_counts())
print(data.groupby("Cluster").mean())

plt.scatter(data["QUANTITYORDERED"], data["SALES"], c=data["Cluster"])
plt.xlabel("Quantity Ordered")
plt.ylabel("Sales")
plt.title("K-Means Clusters")
plt.show()

plt.xlabel("Sales (scaled)")
plt.ylabel("Quantity Ordered (scaled)")
plt.title("Sales Data Clustering")
plt.show()
