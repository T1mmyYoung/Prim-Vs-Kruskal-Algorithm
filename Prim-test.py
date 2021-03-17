#Timothy Young, HW8, CS350
##Prims Algorithm for the MST(Adjacency List using Dictionaries!)
import heapq
import time
from operator import itemgetter,attrgetter

file = open("city-pairs.txt")
vertices = {}
for i in range(30):
    vertexArray = []

edges = []
cities = {}
index = 1
visited = {}
listTuple = []
j = 1

for line in file:
    temp=line.split(' ',maxsplit=2)
    temp[2].rstrip('\n')

    v1 = (temp[0])
    v2 = (temp[1])
    weight = int(temp[2])
    
    
    listTuple.append((v2,weight))
    
    visited[v1] = False
    cities[j] = v1
    
    
    if (index % 28 == 0):
        listTuple.sort(key = itemgetter(1))
        vertices.update({v1:listTuple})
        listTuple = []
        j = j+1

    index = index+1
file.close()

def check(lst=[]):
    t = []
    pq = []
    for i in range(len(lst)):
        t = lst[i]
        city = t[0]
        if(visited[city] == False):
            pq.append(t)
            
    return pq
        
    
def test(str):
    pq = []
    temp = []
    cost = 0
   
    heapq.heappush(pq,vertices[str])
    visited[str] = True
    count = 1
    #breakpoint()
    while(pq and count<29):
        temp = heapq.heappop(pq[0])

        if(visited[temp[0]]!=True):
            cost += temp[1]
            visited[temp[0]] = True
            pq = []
            lst = vertices[temp[0]]
            newCity = check(lst)
            heapq.heappush(pq,newCity)
            count = count+1
        
    
    return cost
#Intended to run the entire graph to find the optimized MST. This implementation finds a MST with a given city, but I could not get the iteration to work.
#cost = []
#for key in cities:
    #cost.append(test(cities[key]))

#for i in range(len(cost)):
    #print('\n')
    #print("City#",i,":",cost[i])