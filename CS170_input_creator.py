import math
import random

g1 = (0,4,5)
g2 = (3,7,8)
g3 = (1,2,6,9)
g4 = 

groupMap = {}
for i in range(0,10):
    if i in g1:
        groupMap[i] = 'g1'
    if i in g2:
        groupMap[i] = 'g2'
    if i in g3:
        groupMap[i] = 'g3'
print(10)
print(36)
for i in range(0,10):
    for j in range(i+1,10):
        if (groupMap[i] == groupMap[j]):
            if groupMap[i] == 'g3':
                print(str(i) + " " + str(j) + " " + "1" + " " + "2")
            else:
                print(str(i) + " " + str(j) + " " + "1" + " " + "4")
        else:
            print(str(i) + " " + str(j) + " " + "99.999" + " " + "7.3")
