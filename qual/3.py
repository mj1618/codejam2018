import sys

def grid_full(grid, x):
    for i in range(3):
        for j in range(3):
            if grid[i+x[0]-1][j+x[1]-1] != 'X':
                return False
    return True

testCases = int(raw_input())
for testCase in range(1, testCases + 1):
    a = int(raw_input())
    grid = []
    curr = [1,1]
    for i in range(1000):
        x=[]
        for j in range(1000):
            x.append('.')
        grid.append(x)

    while True:
        if grid_full(grid, curr):
            curr[1] += 3
            if curr[1] > 998:
                curr[1] = 2
                curr[0] = curr[0] + 3

        print (str(curr[0]+1) + " " + str(curr[1]+1))
        sys.stdout.flush()

        ls = [int(x) for x in raw_input().split()]
        if ls[0]==-1:
            exit()
        if ls[0]==0 and ls[1]==0:
            break
        grid[ls[0]-1][ls[1]-1] = 'X'