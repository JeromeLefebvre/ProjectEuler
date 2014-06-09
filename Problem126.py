from collections import defaultdict
from itertools import combinations_with_replacement

def calculate_layer(x,y,z,L):
    return 2*(2*(L-1)*(x+z)+2*(L-1)*(L+y-2)+x*y+x*z+y*z)

dict1 = defaultdict(int)
# How to pick these numbers?
# Use itertools combinations to do the iteration
# 
max_v = 20000
for L in range(1,100):
    for x in range(1,4500):
        if calculate_layer(x,x,x,L) > max_v:
            break
        for y in range(x,5000):
            if calculate_layer(x,y,y,L) > max_v:
                break
            for z in range(y,5000):
                if calculate_layer(x,y,z,L) > max_v:
                    break
                print(x,y,z)
                dict1[calculate_layer(x,y,z,L)] += 1
'''
for L in range(1,100):
    for x,y,z in combinations_with_replacement(range(1,5000),3):
        if calculate_layer(x,y,z,L) > max_v:
            break
        dict1[calculate_layer(x,y,z,L)] += 1
'''
print(min(n for n in dict1 if dict1[n] == 1000) == 18522)
