
from math import floor, ceil
from sets import Set
import random

testCases = int(raw_input())

for testCase in range(1, testCases + 1):
    N = int(raw_input())
    ws = map(int, raw_input().split())

    ws = list(reversed(ws))

    seqs=[]
    for i in range(len(ws)+1):
        seqs.append(None)

    L=0

    for i in range(len(ws)):
        w = ws[i]
        for l in reversed(range(min(L+1, len(seqs)-1))):
            if l == 0:
                z = ([w], w*6)
                if seqs[1] is None or seqs[1][1] < z[1]:
                    seqs[1] = z
                if l+1 > L:
                    L = l+1
            else:
                x = seqs[l]
                if x is not None:
                    y = (x[0] + [w], min(x[1] - w, w*6))
                    if y[1] >= 0:
                        if seqs[l+1] is None or seqs[l+1][1] < y[1]:
                            seqs[l+1] = y
                            if l+1 > L:
                                L = l+1

    # (weight, minweightleft)
    print "Case #" + str(testCase) + ": "+str(L)

