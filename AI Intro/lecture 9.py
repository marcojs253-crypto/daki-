import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#nyt for i dag
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import seaborn as sns
from pandas.plotting import scatter_matrix

'''
blobs_data = pd.read_csv("blobs.csv")


X = blobs_data[['Feature1', 'Feature2' ]].values
y = blobs_data['labels'].values
blobs_data = blobs_data.dropna()

labels_blobs = blobs_data['labels'].values # Note: I virkelige clustering-opgaver har man typisk ikke labels -> her bruges de kun for at kunne visualisere, hvor godt metoderne genfinder de naturlige grupperinger


# plt.figure(figsize=(6,6))
# plt.scatter(X[:, 0], X[:, 1], c=labels_blobs, cmap='viridis')
# plt.title("Blobs Dataset")
# plt.xlabel("Feature 1")
# plt.ylabel("Feature 2")
# plt.show()

scaler = StandardScaler()   
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42) # OBS: Husk at tilpasse antal klasser ift. Hvilket datasæt I bruger
kmeans_labels = kmeans.fit_predict(X_scaled)


dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_blobs, cmap='viridis')
axes[0].set_xlabel("Feature 1")
axes[0].set_ylabel("Feature 2")
axes[0].set_title("Original Data (true labels)")
axes[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_labels, cmap='viridis')
axes[1].set_xlabel("Feature 1")
axes[1].set_ylabel("Feature 2")
axes[1].set_title("KMeans Clustering")
axes[2].scatter(X_scaled[:, 0], X_scaled[:, 1], c=dbscan_labels, cmap='viridis')
axes[2].set_xlabel("Feature 1")
axes[2].set_ylabel("Feature 2")
axes[2].set_title("DBSCAN Clustering")

# plt.tight_layout()
# plt.show()

# noisy_circles
noisy_data = pd.read_csv("noisy_circles.csv")
X = noisy_data[['Feature1', 'Feature2' ]].values
y = noisy_data['labels'].values
noisy_data = noisy_data.dropna()

labels_noisy = noisy_data['labels'].values


kmeans = KMeans(n_clusters=2, random_state=42) # OBS: Husk at tilpasse antal klasser ift. Hvilket datasæt I bruger
kmeans_labels = kmeans.fit_predict(X_scaled)
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)


# plt.figure(figsize=(6,6))
# plt.scatter(X[:, 0], X[:, 1], c=labels_noisy, cmap='viridis')
# plt.title("Blobs Dataset")
# plt.xlabel("Feature 1")
# plt.ylabel("Feature 2")
# plt.show()

scaler = StandardScaler()   
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42) # OBS: Husk at tilpasse antal klasser ift. Hvilket datasæt I bruger
kmeans_labels = kmeans.fit_predict(X_scaled)


dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_blobs, cmap='viridis')
axes[0].set_xlabel("Feature 1")
axes[0].set_ylabel("Feature 2")
axes[0].set_title("Original Data (true labels)")
axes[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_labels, cmap='viridis')
axes[1].set_xlabel("Feature 1")
axes[1].set_ylabel("Feature 2")
axes[1].set_title("KMeans Clustering")
axes[2].scatter(X_scaled[:, 0], X_scaled[:, 1], c=dbscan_labels, cmap='viridis')
axes[2].set_xlabel("Feature 1")
axes[2].set_ylabel("Feature 2")
axes[2].set_title("DBSCAN Clustering")

# plt.tight_layout()
# plt.show()
'''

###### opgave 2


Mall_Customers_data = pd.read_csv("Mall_Customers.csv")


#info om sætte

# print(Mall_Customers_data.head())
# print(Mall_Customers_data.shape)
# print(Mall_Customers_data.isna().sum())
# print(Mall_Customers_data.describe())


X = Mall_Customers_data[['Annual Income (k$)', 'Spending Score (1-100)']].values

plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Inertia
k_values = range(2, 11) # Starter fra 2 (inklusiv) til 11 (eksklusiv) - Så vi får en list med k fra 2 til 10

inertias = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(k_values, inertias, marker='o')
plt.title("Elbow Method (Inertia vs. Number of Clusters)")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia (SSE)")
plt.grid(True)
plt.show()


# Silhouette Scores
sil_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels)
    sil_scores.append(sil)


# Plot Silhouette Score
plt.subplot(1,2,2)
plt.plot(k_values, sil_scores, marker='o', color='orange')
plt.title("Silhouette Score")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.grid(True)
plt.tight_layout()
plt.show()

# Choose best k
best_k = k_values[sil_scores.index(max(sil_scores))]
kmeans = KMeans(n_clusters=best_k, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Plot K-Means clusters
plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=kmeans_labels, cmap='viridis')
plt.title(f"K-Means Clusters (k={best_k})")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()

# 5 er den bedste K-værdi det vil sige at de er 5 forskelle forbrugstyper i centeret






print(kmeans_labels.shape)
print(Mall_Customers_data.shape)
Mall_Customers_data['cluster'] = kmeans_labels # laver en ny kolone, efter hvilken grupeing


groups = Mall_Customers_data.groupby('cluster')
for name, group in groups:
    print(f"Cluster {name}:")
    print(group[['Annual Income (k$)', 'Spending Score (1-100)']].describe())
    print()

# Boxplot for Annual Income
plt.figure(figsize=(8,6))
sns.boxplot(x='cluster', y='Annual Income (k$)', data=Mall_Customers_data)
plt.title("Annual Income per Cluster")
plt.show()

# Boxplot for Spending Score
plt.figure(figsize=(8,6))
sns.boxplot(x='cluster', y='Spending Score (1-100)', data=Mall_Customers_data)
plt.title("Spending Score per Cluster")
plt.show()

scatter_matrix(Mall_Customers_data[Mall_Customers_data.columns[:-1]], figsize=(10,10), diagonal='kde', c=Mall_Customers_data['cluster'], marker='o')
plt.show()

