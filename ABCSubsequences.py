'''

-Hard-
*DP*

Given a string s consisting of only letters 'a', 'b' and 'c', find 
the number of different subsequences that look like 'aaa..abb..bbc..c'
Note: subsequences are considered different if any letter comes from a 
different position of s. 

'''

class Solution:
    def findNumberSubsequences(self, s):
        n = len(s)
        dp_a, dp_ab, dp_abc = [0]*(n+1), [0]*(n+1), [0]*(n+1)
        for i in range(1, n+1):
            if s[i-1] == 'a':                
                dp_a[i] = dp_a[i-1] * 2 + 1
                dp_ab[i] = dp_ab[i-1]
                dp_abc[i] = dp_abc[i-1]
            elif s[i-1] == 'b':
                dp_ab[i] = dp_a[i-1] + dp_ab[i-1]*2
                dp_a[i]  = dp_a[i-1]
                dp_abc[i] = dp_abc[i-1]
            elif s[i-1] == 'c':    
                dp_abc[i] = dp_ab[i-1] + dp_abc[i-1]*2
                dp_a[i] = dp_a[i-1]
                dp_ab[i] = dp_ab[i-1]
            print(i, s[i-1], dp_a[i], dp_ab[i], dp_abc[i])
        return dp_abc[n]

                 


if __name__ == "__main__":
    print(Solution().findNumberSubsequences(s='aabc'))
    print(Solution().findNumberSubsequences(s='aaabc'))
    print(Solution().findNumberSubsequences(s='aabcc'))
