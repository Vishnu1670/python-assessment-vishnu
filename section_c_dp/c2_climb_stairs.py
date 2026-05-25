def step(n):
    dp=[0]*(n+1)    # n = 3 the dp = [0]*(3+1)
                    # dp = [0,0,0,0]
    dp[0] = 1       # dp = [1,0,0,0]
    dp[1] = 1       # dp = [1,1,0,0]
    dp[2] = 2       # dp = [1,1,2,0]

    for i in range (3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]     
        #dp[3] = dp[3-1] + dp[3-2] + dp[3-3]
        #dp[3] = dp[2] + dp[1] + dp[0]
        #dp[3] = [3]
        #dp = [1,1,2,4]
        #There are 4 ways to reach stair 3
        # 1+1+1
        # 1+2
        # 2+1
        # 3

    return dp[i]

print(step(3))

[1]
[1,2]
[2,1]
[3]