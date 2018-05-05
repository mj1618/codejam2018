
from math import floor, ceil
from sets import Set
import random
import sys


testCases = int(raw_input())

for testCase in range(1, testCases + 1):
    N = int(raw_input())

    probs = {}
    chosen = {}
    for i in range(N):
        probs[i]=0
        chosen[i]=0

    for i in range(N):
        ls = map(int, raw_input().split())[1:]
        ls = [l for l in ls if l<N and l>=0 and chosen[l]==0]

        for l in ls:
            probs[l]+=1

        random.shuffle(ls)

        m = None
        for i in range(min(20, len(ls))):
            if m is None or probs[ls[i]] < probs[m]:
                m = ls[i]

        if m is None:
            print "-1"
        else:
            chosen[m]=1
            print str(m)


        sys.stdout.flush()


