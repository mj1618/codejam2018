from math import cos, pi, fabs, sin, sqrt, degrees, atan, acos
import numpy as np
from scipy.spatial import ConvexHull
import itertools

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

# print newtons(
#     lambda x: x*x,
#     lambda x: 2.0*x,
#     1
# )
def find_place(ls, a):
    l = 0
    h = len(ls)-1

    while l<h:
        if ls[mid(l,h)]==a:
            return mid(l,h)
        elif ls[mid(l,h)]>a:
            l = mid(l,h)+1
        else:
            h = mid(l,h)
    if ls[l] > a:
        return l+1
    return l

def permutations(ls):
    return list(itertools.permutations(ls))

# move up, down, diags. 0 is right
def move_dir_8(p, dir):
    if dir==0:
        return [p[0]+1, p[1]]
    if dir==1:
        return [p[0]+1, p[1]-1]
    if dir==2:
        return [p[0], p[1]-1]
    if dir==3:
        return [p[0]-1, p[1]-1]
    if dir==4:
        return [p[0]-1, p[1]]
    if dir==5:
        return [p[0]-1, p[1]+1]
    if dir==6:
        return [p[0], p[1]+1]
    if dir==7:
        return [p[0]+1, p[1]+1]

# rearrange w to get the next string that is larger than w
def next_largest_word(w):
    w = list(w)
    i = len(w)-1
    while i>0 and w[i]<=w[i-1]:
        i-=1
    if i==0:
        return 'no answer'
    i-=1
    m = min([x for (j,x) in enumerate(w) if j>i and w[j]>w[i]])
    start = list(w[:i])
    w = list(w[i:])
    del w[w.index(m)]
    w = list(w)
    w.sort()
    return ''.join(start)+m+''.join(w)

def n_digits(num):
    return int(log10(num))+1

def first_n_digits(num, n):
    return num // 10 ** (int(log10(num)) - n + 1)

def last_n_digits(num, n):
    return num % pow(10, n)

def differences_between_list_items(t):
    return [j-i for i, j in zip(t[:-1], t[1:])]


# rotates a point clockwise in a box shape
# boxi is the index of the box, starting with the outer box
def rotate_pt_around_box(n, m, boxi, pt):
    if pt[0]==boxi:
        if pt[1]==boxi:
            pt[0]+=1
        else:
            pt[1]-=1
    elif pt[0]==boxi+n-1:
        if pt[1]==boxi+m-1:
            pt[0]-=1
        else:
            pt[1]+=1
    elif pt[1]==boxi:
        pt[0]+=1
    elif pt[1]==boxi+m-1:
        pt[0]-=1

