
from itertools import count

def kthSum(a, k):
    return sum(i**k for i in a )

def digits(n):
    return [int(a) for a in str(n)]

def isNearPowerSum(n):
    a = digits(n)
    # Digits are made up of only 1, 0s will not work out.
    if (kthSum(a, 2) == kthSum(a, 3)):
        return False
    for k in count(len(a)):
        s = kthSum(a, k)
        if abs(s - n) == 1: 
            print(n, k, s)
            return True
        if s > n:
            return False
    return False

def S(n):
    return sum(n if isNearPowerSum(n) else 0 for n in range(1, 10**n))

'''
35 2 34
75 2 74
528757 6 528756
629643 6 629642
688722 6 688721
715469 6 715468
30405525 10 30405524
31672867 8 31672868
44936324 8 44936323
63645890 8 63645891
63645891 8 63645892
71419078 8 71419077
73495876 8 73495877
381784152
'''
#for i in range(1,9):
#    print(i, S(i))

print(S(8))