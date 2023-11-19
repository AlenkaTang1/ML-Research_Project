from matplotlib.pyplot import figure
import numpy as np
from numpy.random import randn, rand
import matplotlib.pyplot as plt
import random
from matplotlib import style
style.use('ggplot')  # The styling format from matplotlib


def costCalculation(distances, c_vector, k):    # Calculate the costs
    cost = {}
    for i in range(k):
        cost[i] = sum([distances[j, c_vector[j]]
                       for j in range(distances.shape[0]) if c_vector[j] == i])
    print("The total cost:", sum(cost.values()))
    return cost


def centers_old(x, k):  # Selecting K random mediods
    print('Rows: ', x.shape[0], 'Columns: ', x.shape[1])
    try:
        centers = random.sample(range(x.shape[0]), k)
    except ValueError:
        print('k exceeds the population size')  # In case k exceeds the size
        return None
    print('centers: ', centers)
    return centers


def func(k, x, centers):
    centers = np.array(centers)
    # select the k random medoids pointed by centers from x
    print('\n')
    print('-'*60)
    medoids = [x[i] for i in centers]
    print('Medoids:', medoids)

    # Distance Calulation
    distances = np.zeros((x.shape[0], k))

    for i, h in zip(medoids, range(k)):  # i represents current mediods
        # j contains the indexes to each point in the array x
        for j in range(x.shape[0]):
            distance = sum(abs(x[j]-i))  # Use Manhattan distances
            distances[j, h] = distance
    c_vector = np.zeros((x.shape[0], 1))   # Initialize cluster vector
    c_vector = [np.argmin(distances[i]) for i in range(distances.shape[0])]
    clusters = find_objects_cluster(x, c_vector, k)
    cost = costCalculation(distances, c_vector, k)
    total_cost = sum(cost.values())
    return total_cost, clusters


def find_objects_cluster(x, c_vector, k, printit=False):
    # Finds the elements that correspond to each cluster
    clusters = {}
    for i in range(k):
        clusters[i] = [x[j] for j in range(x.shape[0]) if c_vector[j] == i]
    if printit == True:
        for cluster, val in clusters.items():
            print('Cluster: ', cluster)
            print(val)
    return clusters


def find_medoids(x, c):  # Getting medoids
    medoids = [x[i] for i in c]
    return medoids


def plot(x, cluster, medoids, k):

    plt.figure(figsize=(6, 5), dpi=150)
    cols = ['.r', '.g', '.b', '.c', '.m', '.y', '.k']
    for i in range(k):
        a = np.array(cluster[i])
        plt.plot(a[:, 0], a[:, 1], cols[i % 6])
        plt.plot(medoids[i][0], medoids[i][1], cols[6])


def experiments2d(x, k, iter):
    meds = centers_old(x, k)
    best_clusters = func(k, x, meds)
    second_best = best_clusters
    best_meds = meds
    second_meds = meds
    print(meds)
    for i in range(iter-1):
        meds = centers_old(x, k)
        medoids = func(k, x, meds)
        if medoids[0] < best_clusters[0]:
            second_best = best_clusters
            best_clusters = medoids
            second_meds = best_meds
            best_meds = meds
        if medoids[0] < second_best[0] and medoids[0] > best_clusters[0]:
            second_best = medoids
            second_meds = meds
    print("Medoid:\n", find_medoids(x, best_meds))
    print('Cost: \n', best_clusters[0])
    plot(x, best_clusters[1], find_medoids(x, best_meds), k)
    plt.show()


if __name__ == '__main__':
    Coordinates = np.array([[0, 7], [1, 1], [1, 6], [1, 8], [2, 5], [2, 7], [2, 8], [3, 0], [3, 6], [
        3, 7], [5, 3], [6, 2], [6, 4], [7, 2], [7, 3], [7, 5], [7, 8], [8, 3], [8, 4], [9, 9]])  # Dataset based on given coordinates
    k = 3  # k value
    iter = 50  # Iteration will be 50
    experiments2d(Coordinates, k, iter)
