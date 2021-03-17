#Timothy Young, HW8, CS350
##Prims Algorithm for the MST(Adjacency List using Dictionaries!)
#This file is the main driving script for testing purposes
import time
from test import *

#Newbie timer approach because I ran out of time trying to get these implementations to work. Use Timeit whenevever possible!!!
time1 = time.perf_counter()
cost = test('Eugene')
time2 = time.perf_counter()
totalTime = time2-time1

print("Prim MST Cost: " ,cost)##Print cost of MST given an individual node(city)
print("Prim Total Time:", totalTime, "fractional seconds")#Print the timer



