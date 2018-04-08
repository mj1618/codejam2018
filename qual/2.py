
testCases = int(raw_input())
for testCase in range(1, testCases + 1):
    raw_input()
    line = raw_input().split()
    ls = [int(x) for x in line]
    evens = [x for (i,x) in enumerate(ls) if i%2==0]
    odds = [x for (i,x) in enumerate(ls) if i%2==1]
    evens.sort()
    odds.sort()

    ls = [y for x in map(None,evens,odds) for y in x]

    res = 'OK'
    for i in range(len(ls)-1):
        if ls[i+1] is not None and ls[i]>ls[i+1]:
            res = i
            break

    print("Case #" + str(testCase) + ": "+str(res))
