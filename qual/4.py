from math import cos, pi, fabs, sin, sqrt

r = 0.5/cos(pi/4.0)
r2 = 0.5 / cos(pi/4.0)
def compute(a):
    return 2.0*r * sin(pi/2.0 - a)

def compute2(a):
    xf = 0.5*cos(a)
    xl = r2*cos(pi/4.0 - a)
    th = xl - xf
    # print th
    assert th >=0.0
    # print xf
    # print xl
    # print th
    ts = 2.0 * (th*r)
    rect = 2.0*r * (2.0 * xf)

    return rect + ts

# print compute(0)
# print compute2(0)
# print compute2(pi/4.0)
# # print ""
# print compute2(pi/8.0)
# exit()
# assert abs(compute2(0)-compute(0)) < 0.00000001

testCases = int(raw_input())

def form(x):
    return "{0:.8f}".format(x)

for testCase in range(1, testCases + 1):
    d = float(raw_input())
    res = 0.0

    h = pi / 4.0
    l = 0.0

    # print compute(h)
    # print compute(l)

    if d < 1.4142136:
        while fabs(compute((h-l)/2.0+l) - d) > 0.00000001:
            # print str((h-l)/2.0+l)+": "+str(compute((h-l)/2.0+l)) +" "+ str(fabs(compute((h-l)/2.0+l) - d))
            if compute((h-l)/2.0+l) < d:
                h = (h-l)/2.0+l
            else:
                l = (h-l)/2.0+l

        x = (h-l)/2.0+l
        # print str((h-l)/2.0+l)+": "+str(compute((h-l)/2.0+l)) +" "+ str(fabs(compute((h-l)/2.0+l) - d))
        print("Case #" + str(testCase) + ": ")
        # print x
        print form(0.5* cos(pi/4.0 - x))+" "+form(0.5* sin(pi/4.0 - x))+" "+"0"

        print form(-0.5* sin(pi/4.0 - x))+" "+form(0.5* cos(pi/4.0 - x))+" "+"0"

        print "0 0 0.5"
    else:
        while fabs(compute2((h-l)/2.0+l) - d) > 0.00000001:
            # print str((h-l)/2.0+l)+": "+str(compute2((h-l)/2.0+l)) +" "+ str(fabs(compute2((h-l)/2.0+l) - d))
            if compute2((h-l)/2.0+l) > d:
                h = (h-l)/2.0+l
            else:
                l = (h-l)/2.0+l
            if (h-l)<0.00000000001:
                print 'exiting early'
                exit()
        print("Case #" + str(testCase) + ": ")
        x = (h-l)/2.0+l
        print x
        print form(0.5* cos(x))+" "+form(0.5* sin(x))+" "+"0"

        print form(0.25* sin(x))+" "+form(0.25* cos(x))+" "+form(r/2.0)

        print form(-0.25* sin(x))+" "+form(-0.25* cos(x))+" "+form(r/2.0)

