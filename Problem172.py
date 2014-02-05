

'''
Problem 172
How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?
'''

def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

# There are 9*10**17 possible 18 digits number
total = 9*10**17

# there are 3C18 ways to place 9 digits, plus 3C17 ways of placing 0
total -= 9*binomialCoeff(18,3) + binomialCoeff(17,3)

# but we now removed the way to place 2 sets of 3 digits twice need to use multinomials?


# And now we need to remove the 9 ways of placing 3