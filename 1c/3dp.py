
testCases = int(raw_input())

for testCase in range(1, testCases + 1):
    N = int(raw_input())
    ws = map(int, raw_input().split())
    dp = []
    for i in range(0, len(ws), 1):
        added = False
        w = ws[i]
        last = dp[-1] if len(dp)>0 else 0
        if last <= 6*w:
            dp.append(w + last)
            added = True

        for j in range(len(dp) + (-1 if added else 0) -1, -1, -1):
            dj = dp[j]
            dj1 = dp[j-1] if j>0 else 0
            if w + dj1 < dj and dj1 <= 6*w:
                dp[j] = w + dj1

    print "Case #" + str(testCase) + ": "+str(len(dp))
