from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')  # The styling format from matplotlib

coordinates = np.array([[0, 7], [1, 1], [1, 6], [1, 8], [2, 5], [2, 7], [2, 8], [3, 0], [3, 6], [
    3, 7], [5, 3], [6, 2], [6, 4], [7, 2], [7, 3], [7, 5], [7, 8], [8, 3], [8, 4], [9, 9], ])  # Original Dataset
# Plotting the Original Points
plt.scatter(coordinates[:, 0], coordinates[:, 1])
clustering = DBSCAN(eps=3, min_samples=2).fit(coordinates)
print(clustering.labels_)  # Print clustering labels
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(coordinates[:, 0], coordinates[:, 1],
           c=clustering.labels_)  # ax provides the cluster
plt.show()
