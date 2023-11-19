from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
coordinates = np.array([[0, 7], [1, 1], [1, 6], [1, 8], [2, 5], [2, 7], [2, 8], [3, 0], [3, 6], [
    3, 7], [5, 3], [6, 2], [6, 4], [7, 2], [7, 3], [7, 5], [7, 8], [8, 3], [8, 4], [9, 9], ])  # Dataset
labels = range(1, 21)
# Ploting the original data points
plt.figure(figsize=(6, 5))
plt.subplots_adjust(bottom=0.1)
plt.scatter(coordinates[:, 0], coordinates[:, 1], label='True Position')


for label, x, y in zip(labels, coordinates[:, 0], coordinates[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()
# Converting the original plots into hierachal data
link = linkage(coordinates, 'single')

label_list = range(1, 21)

plt.figure(figsize=(6, 5))
dendrogram(link,
           orientation='top',
           labels=label_list,
           distance_sort='descending',
           show_leaf_counts=True)
plt.show()
# Plotting clusters in scatterplot
cluster = AgglomerativeClustering(
    n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit_predict(coordinates)
print(cluster.labels_)  # Prining the labels of the cluster
plt.scatter(coordinates[:, 0], coordinates[:, 1],
            c=cluster.labels_, cmap='rainbow')  # Ploting scatter plot of clusters
plt.show()
