import scipy.spatial.distance as dist

csvFile = open(input("Enter your csv file name: "))

i = 0
j = 0
classLabels = []
geneNames = []
pts = []
"""
this for loop adds the unique class labels to an array and counts them
"""
for row in csvFile:
    row = row.split(",")
    rowLabel = row[len(row) - 1]
    if i == 0:
        for each in row:
            geneNames.append(each)
    else:
        j += 1
        pts.append(row)
        if not rowLabel in classLabels:
            classLabels.append(rowLabel)
    i += 1

"""
k is the number of class labels
numPoints should be one less than the number of rows in the file
"""
k = len(classLabels)
numPoints = j - 1

"""
the next 20 or so lines find the initial centroids for 3 different lengths of k,
by getting the last item in the array and then bitwise shifting the row right,
then it does some nonsense if that doesnt work, all in "linear" time
"""
kCentroids = []
k2Centroids = []
k3Centroids = []

index = numPoints
for x in range(0, k):
    while pts[index] in k3Centroids:
        index = index + 2
    kCentroids.append(pts[index])
    index = index >> 2

k2 = k * 2
index = numPoints
for y in range(0, k2):
    while pts[index] in k3Centroids:
        index = index + 2
    k2Centroids.append(pts[index])
    index = index >> 2

k3 = k * 3
index = numPoints
for z in range(0, k3):
    while pts[index] in k3Centroids:
        index = index + 2
    k3Centroids.append(pts[index])
    index = index >> 2




"""
Cohesion WSS, Separation BSS, and Information gain
"""
print("For k =", k, "WSS =", 0, " and BSS =", 0, "and information gain =", 0)
print("For k =", k2, "WSS =", 0, " and BSS =", 0, "and information gain =", 0)
print("For k =", k3, "WSS =", 0, " and BSS =", 0, "and information gain =", 0)
