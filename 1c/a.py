
from math import floor, ceil
from sets import Set
import random

testCases = int(raw_input())

def find_next_word(N, L, ls, given, curr):
    # print 'curr word: '+curr
    if curr in given:
        return False

    if len(curr) == L:
        return curr

    for x in ls[len(curr)]:
        res = find_next_word(N, L, ls, given, curr + x)
        if res is not False:
            return res

    return False

for testCase in range(1, testCases + 1):
    (N, L) = map(int, raw_input().split())
    ss=[]
    ls = []
    given = {}

    for i in range(L):
        ls.append(Set([]))

    for i in range(N):
        x = raw_input()
        ss.append(x)
        given[x] = True
        for i in range(L):
            ls[i].add(x[i])


    for i in range(L):
        ls[i] = list(ls[i])
        random.shuffle(ls[i])


    res = "-"

    word = find_next_word(N, L, ls, given, "")
    if word is not False:
        res = word

    print "Case #" + str(testCase) + ": "+str(res)