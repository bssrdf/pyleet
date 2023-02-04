'''

-Medium-

*Greedy*
有NN堆纸牌，编号分别为 1,2,…,N。每堆上有若干张，但纸牌总数必为N的倍数。可以在任一堆上取若干张纸牌，然后移动。

移牌规则为：在编号为1堆上取的纸牌，只能移到编号为2的堆上；在编号为N的堆上取的纸牌，只能移到编号为N-1
的堆上；其他堆上取的纸牌，可以移到相邻左边或右边的堆上。

现在要求找出一种移动方法，用最少的移动次数使每堆上纸牌数都一样多。

例如N=4，4堆纸牌数分别为：

①9②8③17④6

移动3次可达到目的：

从 ③ 取4张牌放到 ④ （9,8,13,10）-> 从 ③ 取3张牌放到 ②（9,11,10,10）-> 从 ② 取1张牌放到①（10,10,10,10）。

输入格式
两行

第一行为：NN（NN 堆纸牌，1 \le N \le 1001≤N≤100）

第二行为：A_1,A_2, … ,A_nA 
1
​
 ,A 
2
​
 ,…,A 
n
​
  （NN堆纸牌，每堆纸牌初始数，1 \le A_i \le 100001≤A 
i
​
 ≤10000）

输出格式
一行：即所有堆均达到相等时的最少移动次数。



'''


class Solution(object):

    def divideIntoEvenPiles(self, cards):
        n = len(cards)
        total = sum(cards)
        if total % n != 0: return -1
        target = total // n
        res = 0
        print(total, target)
        for i in range(n):
            temp = cards[i] - target
            if temp != 0:
                cards[i+1] += temp
                res += 1
            print(i, cards[i], temp)
        return res


if __name__ == "__main__":
    print(Solution().divideIntoEvenPiles([9, 8, 17, 6]))
    print(Solution().divideIntoEvenPiles([11, 9, 10, 14, 6]))
