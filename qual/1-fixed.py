def compute(s):
    sum=0
    curr=1
    for (i,c) in enumerate(s):
        if c=='C':
            curr*=2
        else:
            sum+=curr
    return sum

def n_c(s):
    return len([c for c in s if c=='C'])

def can_hack(s):
    return s.find('C') < s.rfind('S')

def hack(s):
    x = -1
    for (i,c) in reversed(list(enumerate(s))):
        if i<len(s)-1 and i>=0 and s[i]=='C' and s[i+1]=='S':
            x = i
            break
    return s[:x]+'S'+'C'+s[x+2:]

testCases = int(raw_input())
for testCase in range(1, testCases + 1):
    line = raw_input().split()
    d = int(line[0])
    s = line[1]
    res=-1
    nc = n_c(s)
    if nc==0:
        if compute(s) <= d:
            res = 0
        else:
            res='IMPOSSIBLE'
    else:
        res=0
        while compute(s) > d and can_hack(s):
            s = hack(s)
            res+=1
        if compute(s) <= d:
            pass
        else:
            res = 'IMPOSSIBLE'

    print("Case #" + str(testCase) + ": "+str(res))
