#!/usr/local/bin/python3.3

d = {1: (233168, True),
2: (4613732, True),
3: (6857, True),
4: (906609, True),
5: (232792560, True),
6: (25164150, True),
7: (104743, True),
8: (40824, True),
9: (31875000, True),
10: (142913828922, True),
11: (70600674, True),
12: (76576500, True),
13: (5537376230, True),
14: (837799, True), 
15: (137846528820, True), 
16: (1366, True), 
17: (21124, True), 
18: (1074, True), 
19: (171, True), 
20: (648, True), 
21: (31626, True), 
22: (871198282, True), 
23: (4179871, True), 
24: (2783915460, True), 
25: (4782, True), 
26: (983, True), 
27: (-59231, True),
28: (669171001, True),
29: (9183, True),
30: (443839, True),
31: (73682, True),
32: (45228, True), 
33: (100, True), 
34: (40730, True), 
35: (55, True), 
36: (872187, True), 
37: (748317, True), 
38: (932718654, True), 
39: (840, True), 
40: (210, True), 
41: (7652413, True), 
42: (162, True), 
43: (16695334890, True), ## Needs improvements
44: (5482660, True), ## Needs improvements
45: (1533776805, True),
46: (5777, True),
47: (134043, True),
48: (9110846700, True),
49: (296962999629, True),
50: (997651, True),
51: (121313, True), 
52: (142857, True),
53: (4075, True),
#54: (-1, True), ## Not done
55: (249, True), 
56: (972, True),
57: (153, True),
58: (26241, True), ## clean up the code to use it in other problem 
59: (107359, True), ## Needs work
60: (26033, True), # Needs work
61: (28684, True),
62: (127035954683, True), ## Needs a lot of work
63: (49, True),
64: (1322, True),
65: (272, True), 
#66: (-1, True), ## Not done
67: (7273, True),
#68: (6531031914842725, True), ## Broken somehow
69: (510510, True), ## Can be improved using a factor generated
70: (8319823, True), 
71: (428570, True), 
72: (303963552391, True),
73: (7295372, True),
74: (402, True),
75: (-1, True), 
76: (190569291, True), 
77: (71, True),
78: (55374, True), ## Needs work
79: (73162890, True), 
80: (40886, True),
81: (427337, True), 
82: (260324, True), 
85: (2772, True),
89: (743, True),
98: (18769, True),
100: (756872327473, True),
102: (228, True),
103: (20313839404245, True), # My solution to this problem is garbage
104: (329468, True), 
105: (73702,True), ### NEEDS work
112: (1587000, True), 
119: (248155780267521, True), 
123: (21035, True),
141: (878454337159,True), ## Needs work
142: (1006193, True), ## Needs clean up
197: (1.710637717, True),
206: (1389019170, True)}

'''
Problem 1 Ran in 5.050969775766134e-06
Problem 2 Ran in 0.0009467910276725888
Problem 3 Ran in 0.27001978299813345
Problem 4 Ran in 0.08041415404295549
Problem 5 Ran in 2.502399729564786e-05
Problem 6 Ran in 6.616103928536177e-05
Problem 7 Ran in 0.24788817402441055
Problem 8 Ran in 0.004701603029388934
Problem 9 Ran in 0.10268057201756164
Problem 10 Ran in 0.26801357202930376
Problem 11 Ran in 0.0031050319666974247
Problem 12 Ran in 6.37416140595451
Problem 13 Ran in 9.44779603742063e-05
Problem 14 Ran in 5.535212854971178
Problem 15 Ran in 0.0004050339921377599
Problem 16 Ran in 0.00012366700684651732
Problem 17 Ran in 0.004682193975895643
Problem 18 Ran in 0.00021035503596067429
Problem 19 Ran in 0.0006191250286065042
Problem 20 Ran in 7.672596257179976e-05
Problem 21 Ran in 40.840024453995284
Problem 22 Ran in 0.015475714986678213
Problem 24 Ran in 0.18576748296618462
Problem 25 Ran in 0.001400795008521527
Problem 26 Ran in 0.11766947497380897
'''

from importlib import import_module
from timeit import timeit

for problem in d:
	if d[problem][1]:
		TestAction = import_module("Problem"+str(problem))
		function = getattr(TestAction,"problem"+str(problem))
		time = timeit(function, number=10)/10
		print("Problem " + str(problem) + " Ran in " + str(time))
		# Check if the problem still has a valid solution
		if function() != d[problem][0]:
			print("issue with problem " + str(problem))