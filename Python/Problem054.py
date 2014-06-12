# Here is my shame
# Taken from:http://puttamalac.wordpress.com/2012/05/07/project-euler-54-my-ultra-compact-poker-hand-evaluator/

from collections import Counter

def problem54():
    pairs = [line.split() for line in open("Problem054.txt")]
    values = {r:i for i,r in enumerate('23456789TJQKA')}
    def hand_cmp(hand):
        comp = list(zip(*sorted(((v, values[k]) for k,v in list(Counter(x[0] for x in hand).items())), reverse=True)))
        if len(comp[0]) == 5:
            unicolor = len({x[1] for x in hand}) == 1
            straight = comp[1] == tuple(range(comp[1][0], comp[1][-1]-1, -1))
            comp[0] = (((1,), (3,2,1)),((3,2,0), 5))[straight][unicolor]
        return comp
    return sum( hand_cmp(pair[:5]) > hand_cmp(pair[5:]) for pair in pairs)

from cProfile import run
if __name__ == "__main__":
    run("problem54()")
    print(problem54() == 376)
