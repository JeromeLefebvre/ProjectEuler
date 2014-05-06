
import copy

from itertools import combinations

guessData = '''5616185650518293 ;2 correct
4895722652190306 ;1 correct
2615250744386899 ;2 correct
2659862637316867 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct'''

guesses = []
for l in guessData.split('\n'):
    l = l.rstrip(' correct')
    digits, correct = l.split(';')
    digits = tuple(int(a) for a in digits.rstrip())
    correct = int(correct)
    guesses.append((digits, correct))

guesses.sort(key=lambda x: x[1])

# Create the inital state base on the bad values of the first line

initial = [(None, {a}) for a in guesses[0][0]]


def merge(current, indices, guess):
    newState = []
    for index, (digit, bad) in enumerate(current):
        if index in indices:  # new correct digit
            if digit is not None and guess[index] != digit:
                raise ValueError
            newState.append((guess[index], copy.deepcopy(bad)))
        else:  # New bad state
            if digit in {guess[index]} | bad:  # bad state
                raise ValueError
            newState.append((digit, bad | {guess[index]}))
    return newState

positions = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

global best
best = 0


def findValid(current, level=1):
    global best
    if level > best:
        print(level)
        best = level
        print(current)
    #print("Current: ", current)
    try:
        guess, correct = guesses[level]
    except:
        if all(a[0] is not None for a in current):
            return current
        else:
            return None
    #print("Guess:", guess, correct)
    for indices in combinations(positions, correct):
        #print("Indices: ", indices)
        try:
            newRestrictions = merge(current, indices, guess)
            #print("New: ", newRestrictions)
            found = findValid(newRestrictions, level + 1)
            if found is not None:
                return found
            # print()
            #print("Came back!!")
            # print(current)
            # print(guess)

        except ValueError:
            # print("Failed...")
            pass


#print(merge(initial, (0,), (3,4,1,0,9)))
print(findValid(initial))

# [4, 6, 4, 0, 2, 6, 1, 5, 7, 1, 8, 4, None, 5, 3, 3] is the current solution
# Yet is should be 4640261571849533
