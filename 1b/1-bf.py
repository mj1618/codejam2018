
from math import floor, ceil

eps = 0.0000000001

def calcdx(x, d):
    x = x%1
    if x >= 0.5:
        return -1
    b = (0.5-x) / d
    if (b%1) < eps:
        return int(floor(b))
    return int(ceil(b))

def calc(cs, N):
    sum = 0
    for i in range(len(cs)):
        sum += round(100.0 * cs[i]/float(N))
    return sum

# print calcdx(1234.0, 0.49)
# exit()

testCases = int(raw_input())
for testCase in range(1, testCases + 1):
    (N, L) = map(int, raw_input().split())
    cs = map(int, raw_input().split())
    resp = sum(cs)

    m = N-resp
    d = (100.0/N)%1

    if d<eps:
        cs.append(m)
        print "Case #" + str(testCase) + ": "+str(calc(cs, N))
    elif d>=0.5-eps:
        for i in range(m):
            cs.append(1)
        # print cs
        # print round(100.0 * cs[i]/float(N))
        print "Case #" + str(testCase) + ": "+str(calc(cs, N))
    else:
        xs = [ [calcdx(x/float(N)*100.0, d) , x] for x in cs ]

        for i in range(m):
            xs.append([calcdx(0.0, d), 0])
        xs.sort()
        # print xs
        # print d
        # print calcdx(0.0, d)
        while m>0:
            i=0
            while i<len(xs) and xs[i][0]<=0:
                i+=1

            if i<len(xs) and xs[i][0] <= m:
                if xs[i][0]>0:
                    n = xs[i][0]
                    xs[i][1] += n
                    xs[i][0] = calcdx(xs[i][1]/float(N)*100.0, d)
                    m -= n
            else:
                xs.append([0, m])
                m = 0
            if m==0:
                break
            xs.sort()
        xs.append([0, m])
        m = 0
        # print [x[1] for x in xs]
        print "Case #" + str(testCase) + ": "+str(calc([x[1] for x in xs], N))


    # print str(N)+" "+str(L)+" "+str(cs)
