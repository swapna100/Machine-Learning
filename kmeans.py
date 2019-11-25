#K-Means clustering implementation

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.


# ====
# Define a function that computes the distance between two data points



# import libraries to have functions for get and return data set
import random
import csv
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import distance
def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    # Calculate Euclidean distance.
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))
  
# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def read_data_file(file_address,col1,col2):
    csv_file = pd.read_csv(file_address)
    xy_data = csv_file[[col1,col2]]
    data_list = xy_data.astype(float).values.tolist()
    return data_list
# For Countries
def get_countries(file_address):
    csv_file = pd.read_csv(file_address)
    countries_column = csv_file[['Countries']]
    countries_list = countries_column.astype(str).values.tolist()
    return countries_list
file_to_read = 0 #to initialize the loop
# If the user enters invalid numbers, the loop will continue asking them to enter a number
while file_to_read < 1 or file_to_read > 3:
    file_to_read = int(input("Enter the number of the file you want to read:" +"\n"+
                              "1 : Data from 1953" + "\n"
                              "2 : Data from 2008" + "\n"
                              "3 : Data from both 1953 and 2008"))
    if file_to_read == 1:
        data_list = read_data_file(r"data1953.csv",
                                   'BirthRate(Per1000 - 1953)','LifeExpectancy(1953)')
        countries_list = get_countries(r"data1953.csv")  
    elif file_to_read == 2:
        data_list = read_data_file(r"data2008.csv",
                                   'BirthRate(Per1000 - 2008)','LifeExpectancy(2008)')
        countries_list = get_countries(r"data2008.csv")
    elif file_to_read == 3:
        data_list = read_data_file(r"dataBoth.csv",
                                   'BirthRate(Per1000)','LifeExpectancy')
        countries_list = get_countries(r"dataBoth.csv")
    else:
        print("That is not a valid option.")      

# ====

# Write the initialisation procedure

n_clusters = int(input("Enter the number of clusters you want: "))
n_iterations = int(input("Enter the number of iterations you want: "))

#After we know which file we working with, two sets of data, num of iterations and clusters, we implement the algorithm

kmeans = KMeans(n_clusters = n_clusters, max_iter = n_iterations) #this does the kmeans algorithm part

kmeans.fit(data_list) #the birthrate (x data) and the life expectancy(y data) are fed to the algorithm

centroids = kmeans.cluster_centers_  #centroids are the means of each cluster that all other data will be organized around

cluster_name = kmeans.labels_ #each data point here is given the cluster number to which it belongs to

dist = kmeans.inertia_ #I think this is for the objective function



# ====
# Print out the results

print(dist)

# Plotting starts here, the colors
colours =  ['b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'k.', 'w.'] #this is like a colour map so that each data point can be given a colour for the corresponding cluster
#it belongs to. #The loop below adjusts the colour map for the number of clusters the user chooses
for i in colours:
    while n_clusters > len(colours):
        colours.append(i)
data_clustered = [] #This array will carry the all the data: countries, x/y data and the cluster label
just_values =[] #This array will just carry the x/y data and the cluster label
for i in range(len(data_list)): 
    data_clustered.append([countries_list[i],data_list[i],str(cluster_name[i])])     
    just_values.append([data_list[i],str(cluster_name[i])])
    plt.plot(data_list[i][0],data_list[i][1],colours[cluster_name[i]],markersize=10) #data is plotted to a graphy
plt.scatter(centroids[:,0],centroids[:,1], marker = "*", color = "black") #markers for the clusters are added
plt.xlabel('BirthRate')
plt.ylabel('Life Expectancy')
plt.show() #to display the figure
#Now we need to organize the data by way of which cluster it belongs too
cluster_list = [] #list of cluster symbols i.e. 0, 1, 2 etc
for i in range(n_clusters): 
    cluster_list.append(str(i))
#Now a dictionary will be made with the keys being the cluster numbers, and the keys will have the corresponding data lists
clust_for_values = {key:[] for key in cluster_list}
data_values = clust_for_values.items() #for each key a list is created
for i in data_values: #iterating through the number of lists there will be for each key
    for j in just_values:  #the x/y data will be used as the lists filled in for each cluster > without the countries, so iteration happening through this list
        if i[0] == j[1]: #if the cluster key matches the cluster label in the x/y data
            i[1].append(j[0]) #then the x/y data pair gets appended to the list for the corresponding cluster group
#I am also making another dictionary like the above but using the data with the countries and x/y data
clus_dict = {key:[] for key in cluster_list} 
clust_data = clus_dict.items() #returns a list of items for each key in the dictionary
for i in clust_data: 
    for j in data_clustered:
        if i[0] == j[2]: 
            i[1].append(j[0:2])
#The separate dictionaries are so that the below queries can be answered better.
for i in clust_data: #basically just counting how many records are in each cluster group
    print("-------------------------------------------------------------------------------------------------")
    print("There are " + str(len(i[1])) + " countries in cluster" + str(i[0]))
    print("-------------------------------------------------------------------------------------------------")
for key, value in clust_data: #Here I use the loop to get the countries in each cluster
    print("-------------------------------------------------------------------------------------------------")
    print("These are the countries that fall in cluster " + str(key[0]) + ":" + "\n")
    for list_ in value:
        print(list_[0])
        print("--------------------------------")
print("\n")
