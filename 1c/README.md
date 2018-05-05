# codejam2018

## Round 1c

I didn't make it through the prev 2 qual rounds, but I came 896 in this one and got through!
I had to deal with a production issue during round 1a.
I completely bombed round 1b due to it starting at midnight, I hit a rounding issue in python and I was printing doubles instead of ints in the result!

What was the rounding error? Try putting this in your py interpreter:
`python
from math import ceil
ceil((0.5 - 10.1%1) / 0.1)
`
I learnt that one the hard way!

### Problem 1 - A Whole New World

This was the simplest problem to solve. Basically you can simplify this problem to the following:
You have N stages (maximum 10)
Each stage you can choose from a list of characters (maximum 26)
Find a word that isn't in a list of excluded words (maximum 2000 excluded words)

The recursive solution was really neat for this one, I was guaranteed not to hit a stack limit as the maximum levels is 10.

`python
# only 'curr' is not a constant
def find_next_word(N, L, ls, given, curr):
    if curr in given: # if in the excluded words list return False
        return False

    if len(curr) == L: # if we're at the last stage we have a winner!
        return curr

    for x in ls[len(curr)]: # go through all the chars in the next stage
        res = find_next_word(N, L, ls, given, curr + x) # recurse with curr+x
        if res is not False:
            return res

    return False
`

Given there is only 2000 exlcuded words, I wasn't too worried about hitting the worst case scenario of 26^10 words, we're bound to find one that works well before then!

### Problem 3 - Ant Stack
I did this problem next as I figured I might be able to get the small problem set out.

This one I recognised as a longest increasing subsequence problem, except with a twist. I knew I had to implement longest increasing subsequence because the worst case had N as 10^5, meaning the algo was probably O(N log(N)).

The twist was there was also a condition between the elements - the sum of the rest of the elements had to be a maximum of 6 times the weight of the current element.

I barely understand longest increasing subsequence, I knew I had no chance of producing the optimal soln to this. So I implemented a bruteforce solution that ran fast enough for the small problem set. And I was done with this problem pretty soon after that!

### Problem 2 - Lollipop shop

This one was a bit tricky, but turned out to be solevd with a bit of luck.

So you have to iterate N times for each input, no way around that. But you also have to iterate N times to search through all the "lollipops" to find the one that has the minimum number of favourites.

This caused my soln to time out. My solution was simple:
Instead of iterating N times to find the true minimum, iterate 20. It's an order of magnitude better than the worst case, which I guessed would bring my soln under the time limit.

I figured the problem writers would try to stop this by making this particular soln fail with cleverly crafted problems. So instead of iterating the first 20 I shuffled and iterated a random 20.

Submitted, completely expecting it to fail, it passed. Wtf! :D
