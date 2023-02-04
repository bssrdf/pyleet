'''
-Medium-

*Difference Array*
*Sliding Window*

链接：https://www.nowcoder.com/questionTerminal/c0803540c94848baac03096745b55b9b
来源：牛客网

我叫王大锤，是一名特工。我刚刚接到任务：在字节跳动大街进行埋伏，抓捕恐怖分子孔连顺。
和我一起行动的还有另外两名特工，我提议

1. 我们在字节跳动大街的N个建筑中选定3个埋伏地点。
2. 为了相互照应，我们决定相距最远的两名特工间的距离不超过D。

我特喵是个天才! 经过精密的计算，我们从X种可行的埋伏方案中选择了一种。这个方案万无一失，
颤抖吧，孔连顺！
……
万万没想到，计划还是失败了，孔连顺化妆成小龙女，混在cosplay的队伍中逃出了字节跳动大街。
只怪他的伪装太成功了，就是杨过本人来了也发现不了的！

请听题：给定N（可选作为埋伏点的建筑物数）、D（相距最远的两名特工间的距离的最大值）以及
可选建筑的坐标，计算在这次行动中，大锤的小队有多少种埋伏选择。
注意：
1. 两个特工不能埋伏在同一地点
2. 三个特工是等价的：即同样的位置组合(A, B, C) 只算一种埋伏方法，不能因“特工之间互
换位置”而重复使用


输入描述:
第一行包含空格分隔的两个数字 N和D(1 ≤ N ≤ 1000000; 1 ≤ D ≤ 1000000)

第二行包含N个建筑物的的位置，每个位置用一个整数（取值区间为[0, 1000000]）表示，
从小到大排列（将字节跳动大街看做一条数轴）

Example 1
输入
4 3
1 2 3 4
输出
4
说明
可选方案 (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)

Example 2

输入
5 19
1 10 20 30 50
输出
1
说明
可选方案 (1, 10, 20)

输出描述:
一个数字，表示不同埋伏方案的数量。结果可能溢出，请对 99997867 取模

1 <= N <= 1000000
1 <= D <= 1000000

'''
class Solution(object):

    def numDeploymentsSlidingWindow(self, N, D, positions):
        n, dist = N, D
        nums = positions        
        res = 0
        left = 0
        right = 2
        
        while left < n-2:
            while right < n and nums[right] - nums[left] <= dist:
                right += 1
            if right - 1 - left >= 2:
                num = right - left - 1
                res += num * (num - 1) // 2
            left += 1
        
        return (res % 99997867)

    def numDeployments(self, N, D, positions):
        """
        type N: int
        type D: int
        type positions: List[int]
        rtype: int
        """
        n = 1000001
        MOD = 99997867
        diff = [0]*n
        for p in positions:
            diff[p] += 1
            diff[n-1] -= 1
        nds = diff       
        for i in range(1, n):
            t = diff[i]
            nds[i] = nds[i-1] + t
        def calc(m):
            return m*(m-1)*(m-2)//6
        last = 0
        res = 0
        for p in positions:
            #print(p, nds[p+D], nds[p-1], nds[p+D]-nds[p-1])
            num = nds[p+D]-nds[p-1]
            if num < 3: continue
            cur = calc(num)
            if last > p:
                dups = nds[last]-nds[p-1]
                cur -= calc(dups)
            res = ((res+cur)%MOD+MOD)%MOD
            last = p + D
        return res



if __name__ == "__main__":
    print(Solution().numDeployments(4, 3, [1,2,3,4]))
    print(Solution().numDeployments(5, 19, [1,10,20,30,50]))
    print(Solution().numDeploymentsSlidingWindow(4, 3, [1,2,3,4]))
    print(Solution().numDeploymentsSlidingWindow(5, 19, [1,10,20,30,50]))