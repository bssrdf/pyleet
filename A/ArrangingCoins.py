'''
You have a total of n coins that you want to form in a staircase shape, where 
every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        the problem boils down to 
        Find the maximum k such that k(k + 1)/2 <= N
        '''
        left, right = 0, n
        while left <= right:
            k = (left + right) // 2
            l = k*(k+1) // 2
            if l == n:
                return k
            if n < l:
                right = k-1
            else:
                left = k+1 
        return right

if __name__ == "__main__":
    print(Solution().arrangeCoins(5))
    print(Solution().arrangeCoins(8))
    
    
