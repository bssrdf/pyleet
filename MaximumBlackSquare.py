'''
-Medium-
*DP*

给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是
子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。
若无满足条件的子方阵，返回空数组。

示例 1:

输入:
[
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
示例 2:

输入:
[
   [0,1,1],
   [1,0,1],
   [1,1,0]
]
输出: [0,0,1]
提示：

matrix.length == matrix[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-black-square-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''
from typing import List

class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        # dp[i][j][0] the number of 0's above [i,j]
        # dp[i][j][1] the number of 0's to the left of [i,j]
        ans = []
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 0:
                    dp[i][j][0] = dp[i-1][j][0] + 1
                    dp[i][j][1] = dp[i][j-1][1] + 1
                    upper = min(dp[i][j][0], dp[i][j][1])
                    for k in range(upper):
                        if min(dp[i-k][j][1], dp[i][j-k][0]) >= k + 1:
                            if not ans or k + 1 > ans[2]:
                                ans = [i-k-1, j-k-1, k + 1]

        return ans
if __name__ == "__main__":
    matrix = [
   [1,0,1],
   [0,0,1],
   [0,0,1]]
    print(Solution().findSquare(matrix))

