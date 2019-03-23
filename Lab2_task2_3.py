####################################
# COSC710                          #
# Lab2: task 2 and 3               #
# Author: Yi-Shan Shir             #
####################################

# This script was run on jupyter notebook, so not receiving network names from sys.arg

## Task2 ##
import numpy as np
import pandas as pd


network = "%s" %"jazz" 
nw = np.loadtxt(network + ".nci").astype(int)

group = np.unique(nw[1:,1])
list_group = [];

for g in group:   
   list_group.append(nw[(nw[:,1]==g),0])

with open(network + ".cid", "w") as output:
    for a in list_group:
        for i in range(a.size):
           output.write(str(a[i]))
           output.write(' ')
            
        output.write('\n')


## Task3 ##

# read the cid file into a list
temp = open(network + ".cid", "r").read().splitlines()

# save the number of groups
num_group = len(temp)

list_of_group = []
for i in range(num_group):
    temp1 = temp[i].split(' ') # split str items in the list into a sub-list
    list_of_group.append(np.asarray(temp1)[0:-1].astype(np.int)) # convert the sub-list into an array of int

# read the edge file
edge = np.loadtxt(network + ".txt").astype(int)

edge_group = []

for i in range(num_group):
    temp_arr = np.zeros((1, 2)).astype(int)
    for j in range(edge.shape[0]):        # edge.shape[0] returns the row numbers
        a = list_of_group[i]              # a = each array in list_of_group
        row = edge[j,:]                   # check every row
        if min(abs(row[0]-a)) + min(abs(row[1]-a)) == 0:   # if (row[0]-a[?] = 0), then row[0] is in a
            temp_arr = np.append(temp_arr,row.reshape(1,2),axis=0)  # originally, row.shape=(2,) --> a vector
            
    edge_group.append(temp_arr[1:,:])  # put each array of edge pairs into a list

# write each array to a .csv
for i in range(len(edge_group)):
    filename = network + "_com%d.csv" % (i+1)
    df = pd.DataFrame(edge_group[i])
    df.to_csv(filename, index=False, header=False, sep=';')
