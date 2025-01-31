#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from collections import Counter


# In[2]:


from collections import Counter
import numpy as np

class KNN:
    
    def eucledian_distance(self, x1, x2):  # Add 'self' here to indicate it's an instance method
        return np.sqrt(np.sum((x1 - x2) ** 2))
    
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
    def predict(self, X):  # Prediction happens by finding the k nearest data points
        predicted_labels = [self._predict(x) for x in X]  # Use X here instead of x
        return np.array(predicted_labels)
    
    def _predict(self, x):  # Helper function to calculate distance and find k-nearest neighbors
        # Compute distances
        distances = [self.eucledian_distance(x, x_train) for x_train in self.X_train]
        
        # Get k nearest samples and their labels
        k_indices = np.argsort(distances)[:self.k] #This sorts the distances calulated in the ascending order in such a way that the position is sorted.
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Majority vote
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
        


# In[ ]:




