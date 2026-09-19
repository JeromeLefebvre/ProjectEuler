
# https://projecteuler.net/problem=684
def s(n):
    remainder = n % 9
    quotient = (n - n % 9)//9
    return int(str(remainder) + '9'*quotient)

'''
def s(n, p):
    remainder = n % 9
    quotient = (n - n % 9)//9
    return int(str(remainder) + '9'*quotient) % p
'''
def S(n,p):
    return sum(s(i,p) % p for i in range(1,n+1))

#print(s(10))
#print(s(13))
#print(S(20))

def fib(n):
    a,b = 1,1
    for _ in range(n):
        yield a
        a, b = b, a + b

for f in fib(90):
    pass
    #print(f)
    #print(S(f, 100000007) % 100000007)

#print(s(2880067194370816120))

l = []
for index, power in enumerate(range(1,100000)):
    a = (10**power) % 100000007
    if a in l:
        print("index", index)
    l.append(a)
    #print(a)


'''
To do find phi(10000007) to help compute 10**n mod 10000007 fast

'''