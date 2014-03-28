#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=186
Connectedness of a network
Problem 186
'''

'''
Notes on problem 186():
'''

from memoize import memoize

@memoize
def s(k=1):
    '''A function that returns a caller'''
    if k <= 55:
        return (100003 - (200003*k % 10**6) + (300007*pow(k,3,10**6) % 10**6)) % 10**6
    else:
        return (s(k-24) + s(k-55)) % 10**6

from itertools import count
def dialing():
    for k in count(1,2):
        yield s(k), s(k+1)

def problem186():
    friendsOfPM = {n:False for n in range(0,10**6)}
    friendsOfPM[524287] = True
    friends = {n:set() for n in range(0,10**6)}
    numberOfCalls = 0
    friendsSoFar = 1
    for index, calls in enumerate(dialing()):
        caller, called = calls
        if caller == called: continue # missdialed
        numberOfCalls += 1
        # If they are friends, then set friends to be true
        allFriends = {called} | {caller} | friends[called] | friends[caller]
        friends[caller] = allFriends
        friends[called] = allFriends
        if any( friendsOfPM[person] for person in allFriends ):
            for person in allFriends:
                friends[person] = set()
                if not friendsOfPM[person]:
                    friendsSoFar += 1               
                    friendsOfPM[person] = True  
        #print(caller, friends[caller], friendsOfPM[caller], called, friends[called], friendsOfPM[called])
        print(friendsSoFar, index)
        if friendsSoFar >= (10**6)*0.99:
            return numberOfCalls

def problem186():
    friends = {n:{n} for n in range(0,10**6)}
    numberOfCalls = 0
    PM = 524287
    for index, calls in enumerate(dialing()):
        caller, called = calls
        if caller == called: continue # missdialed
        numberOfCalls += 1
        # If they are friends, then set friends to be true
        allFriends = {called} | {caller} | friends[called] | friends[caller]
        if friends[caller] != allFriends:
            for friend in allFriends:
                friends[friend] = allFriends
        #print(caller, friends[caller], friendsOfPM[caller], called, friends[called], friendsOfPM[called])
        print(len(friends[PM]), index)
        if len(friends[PM]) >= (10**6)*0.99:
            return numberOfCalls

# Based on http://en.wikipedia.org/wiki/Disjoint-set_data_structure
def problem186():
    graph = [set([i]) for i in range(10**6)] # makeset
    def find(i): # Fidning when the element is
        # if graph[i] is an integer, then it was already joined to an other network
        # Where that network is, is pointed to by the location of graph[i]
        # Can not memoize this function as graph[i] changes each loop
        while isinstance(graph[i], int):
            i = graph[i]
        return i
    gen = dialing()
    numberOfCalls = 0
    PM = find(524287)
    while len(graph[PM]) < 99*10**4:
        caller, called = next(gen)
        if caller == called: continue
        numberOfCalls += 1
        indexCaller = find(caller)
        indexCalled = find(called)
        if indexCaller != indexCalled: # They are not already friends
            toJoin = max(indexCaller, indexCalled) # The friends are merged in some way
            toRemove = min(indexCaller, indexCalled) 
            graph[toJoin] |= (graph[toRemove]) # the union operation
            graph[toRemove] = toJoin  
        PM = find(PM)   # Updat the location of PM in case it was changed
    return numberOfCalls

# Based on http://en.wikipedia.org/wiki/Disjoint-set_data_structure
def problem186():
    graph = [set([i]) for i in range(10**6)] # makeset
    def find(i): # Fidning when the element is
        # if graph[i] is an integer, then it was already joined to an other network
        # Where that network is, is pointed to by the location of graph[i]
        # Can not memoize this function as graph[i] changes each loop
        while isinstance(graph[i], int):
            i = graph[i]
        return i
    gen = dialing()
    numberOfCalls = 0
    PM = find(524287)
    while len(graph[PM]) < 99*10**4:
        caller, called = next(gen)
        if caller == called: continue
        numberOfCalls += 1
        indexCaller, indexCalled = sorted([find(caller), find(called)])
        if indexCaller != indexCalled: # They are not already friends
            #toJoin = max(indexCaller, indexCalled) # The friends are merged in some way, it doesn't seem to matter in which way as long as it is consistent
            #toRemove = min(indexCaller, indexCalled) 
            graph[indexCaller] |= (graph[indexCalled]) # the union operation
            graph[indexCalled] = indexCaller  # Go to 
        PM = find(PM)   # Updat the location of PM in case it was changed
    return numberOfCalls

from cProfile import run
if __name__ == "__main__":
    run("problem186()")
    print(problem186() == 2325629) 