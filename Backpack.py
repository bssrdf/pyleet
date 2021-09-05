'''
-Medium-

Given n items with size A_i, an integer m denotes the size of a backpack. How full you can fill this backpack?

You can not divide any item into small pieces.

样例
Example 1:

Input:

array = [3,4,8,5]
backpack size = 10
Output:

9
Explanation:

Load 4 and 5.

Example 2:

Input:

array = [2,3,5,7]
backpack size = 12
Output:

12
Explanation:

Load 5 and 7.

标签

'''

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        
        f[0][0] = True
        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]
                    
        for i in range(m, -1, -1):
            if f[n][i]:
                return i
        return 0

    def backPackOnSpace(self, m, A):
        # write your code here
        n = len(A)
        f = [False] * (m + 1)
        
        f[0] = True
        for i in range(1, n + 1):
            for j in range(m, A[i-1]-1, -1):
                if j >= A[i - 1]:
                    f[j] = f[j] or f[j - A[i - 1]]
        for i in range(m, -1, -1):
            if f[i]:
                return i
        return 0

if __name__ == "__main__":
    print(Solution().backPack(10, [3,4,8,5]))
    print(Solution().backPackOnSpace(10, [3,4,8,5]))
    print(Solution().backPack(12, [2,3,5,7]))
    print(Solution().backPack(12, [2,3,5,7]))