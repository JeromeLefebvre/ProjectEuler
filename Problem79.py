#!/usr/local/bin/python3.3

'''
Problem 79
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''

'''
Notes on problem 79():
'''

from itertools import permutations

def inSameOrder(key,word):
	good = True
	if word[0] in key and word[1] in key and key.index(word[0]) > key.index(word[1]):
		good = False
	if word[0] in key and word[2] in key and key.index(word[0]) > key.index(word[2]):
		good = False
	if word[1] in key and word[2] in key and key.index(word[1]) > key.index(word[2]):
		good = False
	return good

def mergeKey(keys,word):
	return [key for key in keys if inSameOrder(key,word)]


def problem79():
	keylog = '''319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716'''
	PossibleKeysSoFar = [c for c in permutations(['1','2','3','6','7','8','9','0'])]
	for l in keylog.split('\n'):
		PossibleKeysSoFar = mergeKey(PossibleKeysSoFar,l)
		print(l)
		print('***', PossibleKeysSoFar[0])
	return int(''.join(PossibleKeysSoFar[0]))

if __name__ == "__main__":
	print(problem79())
 