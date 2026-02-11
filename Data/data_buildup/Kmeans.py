import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from kmeans_custom import KMeans

# Load data
with open("Data/KUexam_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]

# Extract embeddings
embeddings = np.array([q["embedding"] for q in questions])

# Normalize embeddings
norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
embeddings_normalized = embeddings / norms

# Parameters matching original notebook
max_iterations = 100
k = 15

# Run custom KMeans clustering
kmeans = KMeans(
    n_clusters=k,
    max_iter=max_iterations,
    normalize=False  # We already normalized manually above
)

# Fit on normalized embeddings
labels = kmeans.fit_predict(embeddings_normalized)
centroids = kmeans.centroids

# Print convergence info
print(f"Converged at iteration {kmeans.n_iter_}")

# Assign cluster_id to questions
for q, cluster_id in zip(questions, labels):
    q["cluster_id"] = int(cluster_id)

# Check specific cluster
cluster_id_tocheck = 0
cluster_0_questions = [
    q for q in questions if q["cluster_id"] == cluster_id_tocheck
]

# Display results
print(f"\n=== Cluster {cluster_id_tocheck} Questions ===")
for i, q in enumerate(cluster_0_questions[:125]):
    print(f"{i+1}. ({q['year']}) {q['cleaned_text']}")

# Display cluster statistics
print(f"\n=== Clustering Statistics ===")
cluster_info = kmeans.get_cluster_info()
print(f"Number of clusters: {cluster_info['n_clusters']}")
print(f"Iterations: {cluster_info['n_iterations']}")
print(f"Inertia: {cluster_info['inertia']:.4f}")
print(f"Cluster sizes: {cluster_info['cluster_sizes']}")
