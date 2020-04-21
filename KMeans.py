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
this for loop turns a list of "strings" into a list of ints
"""
newnew = []
for pnt in pts:
    temp = []
    u = 0
    for each in pnt:
        if u < len(pnt) - 1:
            temp.append(int(each))
        u += 1
    newnew.append(temp)
pts = newnew

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
    while pts[index] in kCentroids:
        index = index + 2
    kCentroids.append(pts[index])
    index = index >> 2

k2 = k * 2
index = numPoints
for y in range(0, k2):
    while pts[index] in k2Centroids:
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


print("Initial centroids for k =", k, "are ")
for each in kCentroids:
    print(each)
print("Initial centroids for k =", k2, "are ")
for each in k2Centroids:
    print(each)                                                
print("Initial centroids for k =", k3, "are ")
for each in k3Centroids:
    print(each)


kEuclideanClusters = []
kManhattanClusters = []
eDistance = 10000
mDistance = 10000
i = 0
#distance computations for k = numClassLabels
for pnt in pts:
    k = 0
    l = 0
    for x in kCentroids:
        thisEDist = dist.euclidean(pnt[0:len(pnt) - 1], x[0:len(x) - 1])
        thisMDist = dist.cityblock(pnt[0:len(pnt) - 1], x[0:len(x) - 1])
        #thisDist = dist.euclidean(pnt, x)
        if thisEDist == 0:
            print()
        elif thisEDist < eDistance:
            eDistance = thisEDist
            k += 1
        if thisMDist == 0:
            print()
        elif thisMDist < mDistance:
            mDistance = thisEDist
            l += 1
        i += 1
    kEuclideanClusters[k].appennd(pnt)
    kManhattanClusters[l].appennd(pnt)


eDistance = 10000
mDistance = 10000
k2EuclideanClusters = []
k2ManhattanClusters = []
#distance computations for k = numClassLabels * 2
for pnt in pts:
    k = 0
    l = 0
    for x in k2Centroids:
        thisEDist = dist.euclidean(pnt[0:len(pnt) - 1], x[0:len(x) - 1])
        thisMDist = dist.cityblock(pnt[0:len(pnt) - 1], x[0:len(x) - 1])
        #thisDist = dist.euclidean(pnt, x)
        if thisEDist == 0:
            print()
        elif thisEDist < eDistance:
            eDistance = thisEDist
            k += 1
        if thisMDist == 0:
            print()
        elif thisMDist < mDistance:
            mDistance = thisEDist
            l += 1
        i += 1
    k2EuclideanClusters[k].appennd(pnt)
    k2ManhattanClusters[l].appennd(pnt)


eDistance = 10000
mDistance = 10000
k3EuclideanClusters = []
k3ManhattanClusters = []
#distance computations for k = numClassLabels * 3
for pnt in pts:
    k = 0
    l = 0
    for x in k3Centroids:
        thisEDist = dist.euclidean(pnt[0:len(pnt) - 1], x[0:len(x) - 1])
        thisMDist = dist.cityblock(pnt[0:len(pnt) - 1], x[0:len(x) - 1])
        #thisDist = dist.euclidean(pnt, x)
        if thisEDist == 0:
            print()
        elif thisEDist < eDistance:
            eDistance = thisEDist
            k += 1
        if thisMDist == 0:
            print()
        elif thisMDist < mDistance:
            mDistance = thisEDist
            l += 1
        i += 1
    k3EuclideanClusters[k].appennd(pnt)
    k3ManhattanClusters[l].appennd(pnt)


"""
Cohesion WSS, Separation BSS, and Information gain       
"""

print("For k =", k, "WSS =", 0, " and BSS =", 0, "and information gain =", 0)
print("For k =", k2, "WSS =", 0, " and BSS =", 0, "and information gain =", 0)
print("For k =", k3, "WSS =", 0, " and BSS =", 0, "and information gain =", 0)
