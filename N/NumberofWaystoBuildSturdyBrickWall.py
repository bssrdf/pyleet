'''
-Medium-

*DP*
*Bitmask*



'''

class Solution:
    def buildWall(self, height, width, bricks): 
        # 本题的突破口在于width<=10，这暗示我们可以用一个10bit的01二进制数来表示“长度为w的线段
        # 可以如何切割为若干段”。那么如何用一串01既来表示“用了哪些长度的砖”、又可以
        # 描述“这些砖是怎么排列的”呢？方法就是着眼于那些可能是切缝的位置。

        # 例如长度为w，就有w-1个潜在的切缝位置（编号是0到w-2），我们用1表示这确实是个两块砖
        # 之间的缝，0则表示这个位置属于一块完整的砖无法切割。特别注意，我们需要虚拟地添加上左
        # 边缘的位置（想象成第-1个切缝位置）和右边缘的位置（想象成第w-1个切缝位置）。

        # 比如w=6，那么内部有五个切缝位置，假设是10010，表示切缝位置0、3是砖与砖的交界处。另外
        # 加上左边缘-1和右边缘5，所以总共有四个交界位置：-1,0,3,5，这说明有三块长度分别是1、3、2的
        # 砖拼接起来。也就是说，任意两个1之间的index之差，表示了中间有多少块砖。

        # 考虑到w很小，我们穷举所有对w的切割方案，看看切割出来的每一小段是否存在于bricks里面。都
        # 存在的话就是一个合法的切割（拼接）方案。

        # 我们得到所有合法的切割方案之后（用bitmask的形式表示），就是常规的状态压缩DP。
        # 我们用dp[i][state]表示第i层用state这种拼接方式的话可以有多少种方案。
        # 显然dp[i][state]+=dp[i-1][state1]其中state1和state不能在同一个切缝位置上都是
        # 拼接点，也就是说必须满足(state & state1) == 0。这个思想和paint house非常相似，
        # 在那道题里，任何相邻的房子不能是同一种颜色。

        # 最终答案是 sum{dp[height-1][state]} for all states
        b = set(bricks)
        plans = []
        m, MOD = width - 1, 10**9+7
        for state in range(1<<m):
            temp = [-1]
            for i in range(m):
                if state & (1 << i):
                    temp.append(i)
            temp.append(m)
            flag = True
            for i in range(1, len(temp)):
                if temp[i]-temp[i-1] not in b:
                    flag = False
                    break
            if flag: plans.append(state)
        n, ret = len(plans), 0
        dp  = [[0]*n for _ in range(height)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, height):
            for j in range(n):
                for k in range(n):
                    if plans[j] & plans[k] == 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
        for j in range(n):
            ret = (ret + dp[-1][j]) % MOD
        return ret       
  

if __name__ == "__main__":
    print(Solution().buildWall(2, 3, [1,2]))