####################################
# COSC710                          #
# Lab2: task 2 and 3               #
# Author: Yi-Shan Shir             #
####################################

import numpy as np

# get rid of the first 3 rows(str) and the 3rd column(weight)
raw = np.loadtxt("jazz.net", skiprows=3, usecols=(0,1)).astype(int)

input_count = raw.shape[0]

# to make sure the node in column 0 is smaller than the node in column 1
for i in range(input_count):
    if raw[i,0] > raw[i,1]:
        temp = raw[i,0]
        raw[i,0] = raw[i,1]
        raw[i,1] = temp

# create an array to store the processed arrays
temp_arr = np.zeros((1, 2)).astype(int)

n = np.unique(raw).shape[0]

# for every unique node in column 0, find the unique node it links to
# save all pairs for every unique node from column 0 to array "temp2",
# then append all the arrays 
for i in range(1,n+1):
    temp0 = raw[(raw[:,0]==i),0]
    temp1 = np.unique(raw[raw[:,0]==i,1])
    temp0 = temp0[0:temp1.shape[0]].reshape(temp1.shape[0],1)
    temp1 = temp1.reshape(temp1.shape[0],1)
    temp2 = np.append(temp0,temp1,axis=1)
    temp_arr = np.append(temp_arr, temp2, axis=0)
    
edge_arr = temp_arr[1:,]  # get rid of [0,0]
np.savetxt("jazz.txt", edge_arr, fmt='%d')
