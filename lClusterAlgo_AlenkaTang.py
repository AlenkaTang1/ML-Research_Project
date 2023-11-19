from sklearn.cluster import SpectralClustering
from numpy import unique
from numpy import where
from matplotlib import pyplot
import numpy as np
from matplotlib import style
style.use('ggplot')  # The styling format from matplotlib

coordinates = np.array([[0, 7], [1, 1], [1, 6], [1, 8], [2, 5], [2, 7], [2, 8], [3, 0], [3, 6], [
    3, 7], [5, 3], [6, 2], [6, 4], [7, 2], [7, 3], [7, 5], [7, 8], [8, 3], [8, 4], [9, 9], ])  # Original Dataset
clf = SpectralClustering(n_clusters=2)
prediction = clf.fit_predict(coordinates)  # fit model for cluster prediction

cluster = unique(prediction)   # Gets the clusters
# Function that plots for each cluster
for i in cluster:
    rowIndex = where(prediction == i)
    pyplot.scatter(coordinates[rowIndex, 0], coordinates[rowIndex, 1])

pyplot.show()
