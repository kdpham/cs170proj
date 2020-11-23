import math
import random

g1 = [0,4,5]
g2 = [3,7,8]
g3 = [1,2,6,9]
g4 = [10+x for x in g1]
g5 = [10+x for x in g2]
g6 = [10+x for x in g3]
g7 = [10+x for x in g4]
g8 = [10+x for x in g5]
g9 = [10+x for x in g6]
g10 = [10+x for x in g7]
g11 = [10+x for x in g8]
g12 = [10+x for x in g9]
g13 = [10+x for x in g10]
g14 = [10+x for x in g11]
g15 = [10+x for x in g12]

groupMap = {}
for i in range(0,50):
    if i in g1:
        groupMap[i] = 'g1'
    if i in g2:
        groupMap[i] = 'g2'
    if i in g3:
        groupMap[i] = 'g3'
    if i in g4:
        groupMap[i] = 'g4'
    if i in g5:
        groupMap[i] = 'g5'
    if i in g6:
        groupMap[i] = 'g6'
    if i in g7:
        groupMap[i] = 'g7'
    if i in g8:
        groupMap[i] = 'g8'
    if i in g9:
        groupMap[i] = 'g9'
    if i in g10:
        groupMap[i] = 'g10'
    if i in g11:
        groupMap[i] = 'g11'
    if i in g12:
        groupMap[i] = 'g12'
    if i in g13:
        groupMap[i] = 'g13'
    if i in g14:
        groupMap[i] = 'g14'
    if i in g15:
        groupMap[i] = 'g15'


print(50)
print(90)
for i in range(0,50):
    for j in range(i+1,50):
        if (groupMap[i] == groupMap[j]):
            if groupMap[i] == 'g3' or groupMap[i] == 'g6' or groupMap[i] == 'g9' or groupMap[i] == 'g12' or groupMap[i] == 'g15':
                print(str(i) + " " + str(j) + " " + "1" + " " + "1")
            else:
                print(str(i) + " " + str(j) + " " + "1" + " " + "2")
        else:
            print(str(i) + " " + str(j) + " " + "99.999" + " " + "3.65")
