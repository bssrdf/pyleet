# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(1, n+1): 
        for w in range(wt[i-1], W+1): 
            K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
    return K[n][W] 

def knapSackSpaceOpt(W, wt, val, n): 
    dp = [0]*(W+1) 
    for i in range(n): 
       #traverse dp array from right to left 
       for j in range(W,wt[i]-1,-1): 
          dp[j] = max(val[i] + dp[j-wt[i]],  dp[j]) 
            #print i, w, K[i][w]
  
    return dp[W] 
  
# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n))
print(knapSackSpaceOpt(W, wt, val, n))
