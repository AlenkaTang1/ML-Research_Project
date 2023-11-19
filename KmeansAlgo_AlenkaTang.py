import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')  # The styling format from matplotlib


class kMeans:
    def __init__(self, k=2, rate=0.001, iterations=300):  # initialize the kMeans class
        self.k = k
        self.iterations = iterations
        self.rate = rate

    def fit(self, dataset):  # Function to fit the dataset (coordinates)
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = dataset[i]

        for i in range(self.iterations):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for set in dataset:
                # distance computation
                distance = [np.linalg.norm(
                    set-self.centroids[centroid]) for centroid in self.centroids]
                classification = distance.index(min(distance))
                self.classifications[classification].append(set)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(
                    self.classifications[classification], axis=0)

            optimized = True

            for j in self.centroids:
                # the original centroid is now the previous
                original_centroid = prev_centroids[j]
                # current centroid is the current mean of all points
                current_centroid = self.centroids[j]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.rate:
                    print(np.sum((current_centroid-original_centroid) /
                                 original_centroid*100.0))
                    optimized = False

            if optimized:  # stop the loop if it is already optimized
                break


coordinates = np.array([[1, 2], [1, 3], [1, 5], [2, 2], [2, 4], [3, 1], [3, 3], [4, 2], [5, 7], [
                       6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [7, 3], [7, 9], [7, 8], [8, 6]])  # Dataset based on given coordinates

colors = 10*["g", "r", "c", "b", "k"]
clf = kMeans()        # Classifier
clf.fit(coordinates)  # Using the coordinate points
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid]
                [1], marker="o", color="k", s=100, linewidths=4)
for classification in clf.classifications:
    color = colors[classification]
    for set in clf.classifications[classification]:
        plt.scatter(set[0], set[1], marker="o",
                    color=color, s=100, linewidths=4)

plt.show()
