from math import cos, pi, fabs, sin, sqrt, degrees, atan, acos
import numpy as np
from scipy.spatial import ConvexHull

def sqrd(x):
    return x*x

xaxis = [1, 0, 0]
yaxis = [0, 1, 0]
zaxis = [0, 0, 1]

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


def mid(l, h):
    return l + abs(h-l)/2


def rotate3d(pt, v, a):
    x = [cos(a)+sqrd(v[0])*(1-cos(a)), v[0]*v[1]*(1-cos(a)) - v[2]*sin(a), v[0]*v[2]*(1-cos(a))+v[1]*sin(a)]
    y = [v[0]*v[1]*(1-cos(a))+v[2]*sin(a), cos(a)+sqrd(v[1])*(1-cos(a)), v[1]*v[2]*(1-cos(a))-v[0]*sin(a)]
    z = [v[2]*v[0]*(1-cos(a))-v[1]*sin(a), v[1]*v[2]*(1-cos(a))+v[0]*sin(a), cos(a)+sqrd(v[2])*(1-cos(a))]
    mapply = [
        [pt[i]*m for (i,m) in enumerate(x)],
        [pt[i]*m for (i,m) in enumerate(y)],
        [pt[i]*m for (i,m) in enumerate(z)]
    ]
    return [sum(m) for m in mapply]

def segments(p):
    return zip(p, p[1:] + [p[0]])

def convex_hull(pts):
    hull = ConvexHull(pts)
    return [pts[i] for i in hull.vertices]

def poly_area(pts):
    pts_hull = convex_hull(pts)
    n = len(pts_hull)
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += abs(pts_hull[i][0] * pts_hull[j][1]-pts_hull[j][0] * pts_hull[i][1])
    result = a / 2.0
    return result

def projected_area_xz(cube):
    pts = [ [pt[0], pt[2]] for pt in cube ]
    return poly_area(pts)

def square(y):
    return [
        [1.0,y,1.0],
        [-1.0,y,1.0],
        [-1.0,y,-1.0],
        [1.0,y,-1.0],
    ]

def newtons(f, g, x, e=1e-8):
    while abs(f(x))>e:
        x -= f(x) / g(x)
    return x

unit_cube = square(0.0) + square(1.0)

print newtons(
    lambda x: x*x,
    lambda x: 2.0*x,
    1
)