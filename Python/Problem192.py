#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=192
Best Approximations
Problem 192
'''

'''
Notes on problem 192():
'''

def farey(x, N):
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = float(a+c)/(b+d)
        if x == mediant:
            if b + d <= N:
                return a+c, b+d
            elif d > b:
                return c, d
            else:
                return a, b
        elif x > mediant:
            a, b = a+c, b+d
        else:
            c, d = a+c, b+d
 
    if (b > N):
        return c, d
    else:
        return a, b

def problem192():
	print(13**(1/2))
	return farey(13**(1/2)/10,30), farey(13**(1/2),20)



from cProfile import run
if __name__ == "__main__":
	#run("problem192()")
	print(problem192()) 
