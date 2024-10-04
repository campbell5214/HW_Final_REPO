import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from scipy.optimize import linear_sum_assignment
import seaborn as sns
import matplotlib.pyplot as plt
from yellowbrick.cluster import KElbowVisualizer
from sklearn.datasets import make_blobs

# TODO 1: Determine the best k for K-means using KElbowVisualizer
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

kmeans = KMeans()
visualizer = KElbowVisualizer(kmeans, k=(2, 10))
visualizer.fit(X)
visualizer.show()

best_k = visualizer.elbow_value_

# TODO 2: Fit K-means with the best K
kmeans = KMeans(n_clusters=best_k)
y_kmeans = kmeans.fit_predict(X)

# TODO 3: Calculate accuracy for best K
def cluster_accuracy(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    row_ind, col_ind = linear_sum_assignment(-cm)
    return cm[row_ind, col_ind].sum() / y_true.size

accuracy = cluster_accuracy(y_true, y_kmeans)
print(f"Accuracy for K={best_k}: {accuracy}")

# TODO 4: Draw a confusion matrix
cm = confusion_matrix(y_true, y_kmeans)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.arange(best_k), yticklabels=np.arange(best_k))
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title(f'Confusion Matrix for K={best_k}')
plt.show()
