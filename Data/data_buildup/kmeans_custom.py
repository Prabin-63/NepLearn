import numpy as np

class KMeans:
    
    def __init__(self, n_clusters=8, max_iter=100, tolerance=1e-6, 
                 normalize=False, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.normalize = normalize
        self.random_state = random_state
        self.centroids = None
        self.labels_ = None
        self.inertia_ = None
        self.n_iter_ = 0
        
    def _initialize_centroids(self, X):
        if self.random_state is not None:
            np.random.seed(self.random_state)
            
        indices = np.random.choice(len(X), size=self.n_clusters, replace=False)
        centroids = X[indices].copy()
        
        if self.normalize:
            centroids = self._normalize(centroids)
            
        return centroids
    
    def _normalize(self, X):
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        # Avoid division by zero
        norms = np.where(norms == 0, 1, norms)
        return X / norms
    
    def _assign_labels(self, X, centroids):
        # Calculate distances: (n_samples, 1, n_features) - (1, n_clusters, n_features)
        # Result: (n_samples, n_clusters)
        distances = np.linalg.norm(X[:, np.newaxis, :] - centroids[np.newaxis, :, :], axis=2)
        labels = np.argmin(distances, axis=1)
        return labels
    
    def _update_centroids(self, X, labels):
        n_features = X.shape[1]
        new_centroids = np.zeros((self.n_clusters, n_features))
        
        for i in range(self.n_clusters):
            cluster_points = X[labels == i]
            
            if len(cluster_points) == 0:
                # Reinitialize empty cluster with a random point
                new_centroids[i] = X[np.random.randint(len(X))]
            else:
                new_centroids[i] = cluster_points.mean(axis=0)
        
        if self.normalize:
            new_centroids = self._normalize(new_centroids)
            
        return new_centroids
    
    def _calculate_inertia(self, X, labels, centroids):
        inertia = 0
        for i in range(self.n_clusters):
            cluster_points = X[labels == i]
            if len(cluster_points) > 0:
                distances = np.linalg.norm(cluster_points - centroids[i], axis=1)
                inertia += np.sum(distances ** 2)
        return inertia
    
    def fit(self, X):
        X = np.asarray(X)
        
        # Normalize input if requested
        if self.normalize:
            X = self._normalize(X)
        
        # Initialize centroids
        self.centroids = self._initialize_centroids(X)
        
        # Iterate until convergence or max iterations
        for iteration in range(self.max_iter):
            old_centroids = self.centroids.copy()
            
            # Assign labels
            self.labels_ = self._assign_labels(X, self.centroids)
            
            # Update centroids
            self.centroids = self._update_centroids(X, self.labels_)
            
            # Check convergence
            if np.allclose(self.centroids, old_centroids, atol=self.tolerance):
                self.n_iter_ = iteration + 1
                break
        else:
            self.n_iter_ = self.max_iter
        
        # Calculate final inertia
        self.inertia_ = self._calculate_inertia(X, self.labels_, self.centroids)
        
        return self
    
    def predict(self, X):
        if self.centroids is None:
            raise ValueError("Model not fitted yet. Call fit() first.")
        
        X = np.asarray(X)
        
        if self.normalize:
            X = self._normalize(X)
        
        return self._assign_labels(X, self.centroids)
    
    def fit_predict(self, X):
        self.fit(X)
        return self.labels_
    
    def get_cluster_info(self):
        if self.labels_ is None:
            raise ValueError("Model not fitted yet. Call fit() first.")
        
        unique, counts = np.unique(self.labels_, return_counts=True)
        
        return {
            'n_clusters': self.n_clusters,
            'n_iterations': self.n_iter_,
            'inertia': self.inertia_,
            'cluster_sizes': dict(zip(unique.tolist(), counts.tolist()))
        }
