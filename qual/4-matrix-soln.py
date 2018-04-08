from math import cos, pi, fabs, sin, sqrt, degrees, atan, acos
import numpy as np
from scipy.spatial import ConvexHull

def sqrd(x):
    return x*x

testCases = int(raw_input())
xaxis = [1, 0, 0]
yaxis = [0, 1, 0]
zaxis = [0, 0, 1]

def segments(p):
    return zip(p, p[1:] + [p[0]])

def poly_area(pts):
    hull = ConvexHull(pts)
    pts_hull = [pts[i] for i in hull.vertices]
    n = len(pts_hull) # of corners
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += abs(pts_hull[i][0] * pts_hull[j][1]-pts_hull[j][0] * pts_hull[i][1])
    result = a / 2.0
    return result

def area(cube):
    pts = [ [pt[0], pt[2]] for pt in cube ]
    return poly_area(pts)

def square(y):
    return [
        [0.5,y,0.5],
        [-0.5,y,0.5],
        [-0.5,y,-0.5],
        [0.5,y,-0.5],
    ]

cube = square(0.5) + square(-0.5)

def rotate(pt, v, a):
    x = [cos(a)+sqrd(v[0])*(1-cos(a)), v[0]*v[1]*(1-cos(a)) - v[2]*sin(a), v[0]*v[2]*(1-cos(a))+v[1]*sin(a)]
    y = [v[0]*v[1]*(1-cos(a))+v[2]*sin(a), cos(a)+sqrd(v[1])*(1-cos(a)), v[1]*v[2]*(1-cos(a))-v[0]*sin(a)]
    z = [v[2]*v[0]*(1-cos(a))-v[1]*sin(a), v[1]*v[2]*(1-cos(a))+v[0]*sin(a), cos(a)+sqrd(v[2])*(1-cos(a))]
    mapply = [
        [pt[i]*m for (i,m) in enumerate(x)],
        [pt[i]*m for (i,m) in enumerate(y)],
        [pt[i]*m for (i,m) in enumerate(z)]
    ]
    return [sum(m) for m in mapply]

def rotate_all(pts, v, a):
    return [rotate(pt, v, a) for pt in pts]

def mid(l, h):
    return l + abs(h-l)/2

def binary_search(f, l, h, e=1e-8):
    while h>l and abs(f(mid(l, h))) > e:
        if f(mid(l,h)) > 0:
            h = mid(l,h)
        else:
            l = mid(l,h)

        if mid(l,h)==h:
            print l
            print h
            print f(mid(l,h))
            print 'couldnt find'
            exit()

    return mid(l,h)

for testCase in range(1, testCases + 1):
    d = float(raw_input())
    print ("Case #" + str(testCase) + ": ")
    pts = [
        [0.5, 0, 0],
        [0, 0, 0.5],
        [0, 0.5, 0]
    ]

    if d < 1.4142136:
        res = binary_search(
            lambda x: area(rotate_all(rotate_all(cube, xaxis, x), zaxis, 0))-d,
            0.0,
            pi/4
        )
        pts = rotate_all(rotate_all(pts, xaxis, res), zaxis, 0)
    else:
        res = binary_search(
            lambda x: area(rotate_all(rotate_all(cube, xaxis, pi/4), zaxis, x))-d,
            0.0,
            0.615479690576
        )
        pts = rotate_all(rotate_all(pts, xaxis, pi/4), zaxis, res)

    for pt in pts:
        print ' '.join([str(p) for p in pt])




