'''
-Medium-

*Backtracking*

The gray code is a binary numeral system where two successive values differ in 
only one bit.

Given a non-negative integer n representing the total number of bits in the code, 
print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size 
             is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

'''

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        参考维基百科上关于格雷码的性质，有一条是说镜面排列的，n位元的格雷码可以从n-1位元的
        格雷码以上下镜射后加上新位元的方式快速的得到
        0  0  -> 00    00   -> 000    
        1  1  -> 01    01   -> 001
           1  -> 11    11   -> 011
           0  -> 10    10   -> 010
                       10   -> 110
                       11   -> 111
                       01   -> 101
                       00   -> 100
 
        """
        res = [0]
        for i in range(n):
            size = len(res)
            for j in range(size-1, -1, -1):
                res.append(res[j] | (1 << i))                                    
        return res


if __name__ == "__main__":
    print(list(map(bin,Solution().grayCode(3))))
