# codejam2018

## Round 1c
https://codejam.withgoogle.com/2018/challenges/0000000000007765/analysis

I didn't make it through the prev 2 qual rounds, but I came 896 in this one and got through!
I had to deal with a production issue during round 1a.
I completely bombed round 1b due to it starting at midnight, I hit a rounding issue in python and I was printing doubles instead of ints in the result!

What was the rounding error? [Check here](rounding-error)

### Problem 1 - A Whole New World

This was the simplest problem to solve. Basically you can simplify this problem to the following:
You have N stages (maximum 10)
Each stage you can choose from a list of characters (maximum 26)
Find a word that isn't in a list of excluded words (maximum 2000 excluded words)

The recursive solution was really neat for this one, I was guaranteed not to hit a stack limit as the maximum levels is 10.

```python
def find_next_word(N, L, ls, given, curr): # only 'curr' is not a constant
    if curr in given: # if in the excluded words list return False
        return False

    if len(curr) == L: # if we're at the last stage we have a winner!
        return curr

    for x in ls[len(curr)]: # go through all the chars in the next stage
        res = find_next_word(N, L, ls, given, curr + x) # recurse with curr+x
        if res is not False:
            return res

    return False
```

Given there is only 2000 exlcuded words, I wasn't too worried about hitting the worst case scenario of 26^10 words, we're bound to find one that works well before then!

### Problem 3 - Ant Stack
I did this problem next as I figured I might be able to get the small problem set out.

This one I recognised as a longest increasing subsequence problem. The worst case had N as 10^5, meaning the algo was probably O(N log(N)). LIS is in fact O(N log(N)). Luckily I didn't try to implement it as it turns out there is a much better DP solution

The twist was there was also a condition between the elements - the sum of the rest of the elements had to be a maximum of 6 times the weight of the current element.

I barely understand LIS, I knew I had no chance of producing the optimal soln to this. So I implemented a bruteforce solution (but similar to LIS) that ran fast enough for the small problem set. And I was done with this problem pretty soon after that!

What I didn't realise is that if you look at the problem backwards it becomes far simpler - I think I might have a crack with this view on it and see if I could've got it right by just taking a different view on the problem!

EDIT:
DP solution is way easier. One thing to realise is the max size of the soln is around 150 - meaning it is safe to iterate the entire soln set every iteration, making the complexity O(N*K) where K is ~150. The solution turns out to be much simpler than LIS - and also much simpler if you iterate forwards over the input, which is backwards according to the problem set.

```python

testCases = int(raw_input())

for testCase in range(1, testCases + 1):
    N = int(raw_input())
    ws = map(int, raw_input().split())
    dp = [] # contains the min sum of all weights up to and including the current index

    # iterate all weights
    for i in range(0, len(ws), 1):
        added = False
        w = ws[i]
        last = dp[-1] if len(dp)>0 else 0

        # add the new weight to the end if it is safe to do so
        if last <= 6*w:
            dp.append(w + last)
            added = True

        # go backwards and update all other weight sums to reduce them if possible
        for j in range(len(dp) + (-1 if added else 0) -1, -1, -1):
            dj = dp[j]
            dj1 = dp[j-1] if j>0 else 0
            if w + dj1 < dj and dj1 <= 6*w:
                dp[j] = w + dj1

    print "Case #" + str(testCase) + ": "+str(len(dp))
```

### Problem 2 - Lollipop shop

This one was a bit tricky, but turned out to be solevd with a bit of luck.

So you have to iterate N times for each input, no way around that. But you also have to iterate N times to search through all the "lollipops" to find the one that has the minimum number of favourites.

This caused my soln to time out. My solution was simple:
Instead of iterating N times to find the true minimum, iterate 20. It's an order of magnitude better than the worst case, which I guessed would bring my soln under the time limit.

I figured the problem writers would try to stop this by making this particular soln fail with cleverly crafted problems. So instead of iterating the first 20 I shuffled and iterated a random 20.

Submitted, completely expecting it to fail, it passed. Wtf! :D


### Rounding error
 Try putting this in your py interpreter:
```python
from math import ceil
ceil((0.5 - 10.1%1) / 0.1)
```
I learnt that one the hard way!

Here's the explanation from my smart friend Rowan (sqweek) -

“Rounding error in python” seems a bit unfair, as the problem is 0.1 cannot be exactly represented under IEEE754 which has nothing to do with python. Pretty sure many languages would give you the same result.
Floating point is a bitch, but there’s better ways to think of it than “rounding error”. If you think about the set of real numbers, there’s an infinite amount of them. But we only have 2^32 floats (or 2^64 doubles) to work with. So each floating point value represents a region of the real number line.
The concept of an exact decimal value doesn’t really exist once you hit the FPU. It just deals with the closest “bin”.
In that sense floating point is much the same as fixed point. The only real difference is that the size of the bins is [numerically] constant with fixed point, whereas the bin size grows/shrinks along with the number’s magnitude in floating point.
Converting floats to strings is surprisingly useful at times, because the formatting routines usually have logic that goes “yeah I know this bin is technically centered on 0.100000000000000000001355252715606880542509 but u know what I’m just going to call that 0.1”
(I’m yet to find a better way to convert a float -> double than going via string. A straight typecast in most languages just puts zeros in the lower 32-bits which is really not what you want when it comes to non-representable decimals)

(Matt: I still blame python)
