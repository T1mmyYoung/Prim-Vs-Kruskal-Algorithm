#Timothy Young, HW8, CS350
#This file is the driving script for testing this implementation of Kruskal's
##algorithm. A text file of city-pairs with weights is read in as a graph. 
##The respective vertices with their edge weights are added to the graph, and then a timer is ran to approximate how long Kruskal performs vs. Prim.
from krushkal import *
import time
cities ={}#Dictionary key for cities
v1 = []#Vertex1 array
v2 = []#Vertex2 array
weight = []#Edge weight array
key = 0#Key for dictionary purposes

index = 0#Also useful for dictionary..
##Parsing the text file
file = open("city-pairs.txt")
for line in file:
    temp=line.split(' ',maxsplit=2)
    temp[2].rstrip('\n')

    v1.append((temp[0]))#Parse the first column of txtfile
    v2.append((temp[1]))#Parse the second column of txtfile
    weight.append(int(temp[2]))#Parse the third column of txtfile as integer
    cities[v1[index]] = key#Update the key, dictionaries cannot have duplicate keys!!

    if (index % 28 == 0):#Barbaric, I know..
        key = key+1
    
    index = index+1
file.close()
#Make the graph the appropriate size given the amount of nodes(cities)
g = Graph(key+1)
#Add all of the edges to the graph with respective weights
for i in range(len(v1)-1):
    g.addEdge(cities[v1[i]],cities[v2[i]],weight[i])
#Print cities for key verification
print(cities)
#Timer for testing purposes. Testing for runtime performance.
time1 = time.perf_counter()
g.KruskalMST()#Calling Krushkal on the graph.
time2 = time.perf_counter()
totalTime = time2-time1#Total time is approximate.
print("Krushkal Total Time:", totalTime, "fractional seconds")

##Attempting to run multiple timeit for better analysis. Will not import function from main. Timeit may not work with graphs..
#if __name__ == "__main__":
    #print("Time for Kruskal x10: ", timeit.timeit('g.KruskalMST()','from main #import KruskalMST,g',number = 10),"fractional seconds")