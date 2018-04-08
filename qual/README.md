# codejam2018

## Qual Round

Problem description:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard

Qual rounds are always a bit of fun because there's no time pressure. Interesting part was the interactive problem this year.

I ended up with a score of 69/100 woohoo ;) - and came in 2574 place / 24589.
The 2 problems I got wrong were the second data sets of the 1st and 4th

### 1. Saving the universe again
https://github.com/mj1618/codejam2018/blob/master/qual/1-fixed.py

This problem I distilled down to a greedy algorithm, swapping the highest value CS combination each iteration.
Unfortunately I messed it up and my code ended up choosing the lowest value rather than the highest.
Anti-greedy.

Hence why I pushed a fix 1-fixed.py with the only change being to look for the last known CS combination.

The crux of this problem is the greedy part to find the best value CS combo:
```python
def hack(s):
    x = -1
    for (i,c) in reversed(list(enumerate(s))):
        if i<len(s)-1 and i>=0 and s[i]=='C' and s[i+1]=='S':
            x = i
            break
    return s[:x]+'S'+'C'+s[x+2:]
```

### 2. Trouble Sort
https://github.com/mj1618/codejam2018/blob/master/qual/2.py

This clicked with me straight away, if you setup a problem with 10 numbers and draw how trouble sort works on a piece of paper the problem becomes clear.
Only odds are sorted together, and only evens are sorted together.

Solution:
1. Sort the odds and evens seperately and zip them back together
```python
evens = [x for (i,x) in enumerate(ls) if i%2==0]
odds = [x for (i,x) in enumerate(ls) if i%2==1]
evens.sort()
odds.sort()
ls = [y for x in map(None,evens,odds) for y in x]
```
2. Then simply find the first occurrence of a high number and then a low number

### 3. Go Gopher!
https://github.com/mj1618/codejam2018/blob/master/qual/3.py

This one was super fun, took a minute to read through the interactive guide.
It turned out this problem was really easy because complexity doesn't play much of a factor.

All I did to draw a good rectangle given the Gopher randomly chooses between 9 squares is just go square by square.
E.g. Pick the first square on the grid - 0,0 - 2,2 - and keep choosing the middle point 1,1 until that square is full.
Then go the next square.

I tested on a=200 and turned out this brute-force style solution was well fast enough.

Not really any super interesting code in this one.

### 4. Cubic UFO
https://github.com/mj1618/codejam2018/blob/master/qual/4.py

Oh man these ones are always tricky for me.
I tend to spend time getting the details right when I have a solution that works.
This one I found a bit hard to visualise without a rubiks cube at hand as well.

For the small dataset I got pretty quick.
You can increase the rectangle made by the cube by tilting it in any direction from being a unit square.
The math is simple here, and finding the angle was simply a binary search.

Computing the area given a tilt angle in 0..pi/4 is:
```python
def compute(a):
    return 2.0*r * sin(pi/2.0 - a)
```
where r is the distance from the center to a corner.
Simple trig says `r * sin(pi/2.0 - a)` is the x-value of the corner when tilted by `a`.
Double that to get the full rectangle size.

The next part was hard, anything above 1.414213 requires a max tilt for the rectangle.
And then an additional tilt on the other axis to make a hexagon.
I worked this out, but then struggled getting the details of the math right.

Where I got up to was to calculate the corners required, and then to add the area of the 2 triangles of the hexagon and then the rectangle in the middle.

This is what I got, but turned out to give wrong results:
```python
def compute2(a):
    xf = 0.5*cos(a)
    xl = r*cos(pi/4.0 - a)
    th = xl - xf
    ts = 2.0 * (th*r)
    rect = 2.0*r * (2.0 * xf)
    return rect + ts
```

Honestly thought I got this right, but going to take some time to dig into where I went wrong.
Will be pushing a fix for this later.
