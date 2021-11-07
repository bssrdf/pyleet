'''
-Easy-

Given a positive integer N, you need to factorize all integers between (1, N].
Then you have to count the number of the total prime numbers.

1<N<=100000

样例
input：6
output：7
explain：2=2, 3=3, 4=2*2, 5=5, 6=2*3, the number of prime number : 1+1+2+1+2=7

'''

class Solution:
    """
    @param N: a number
    @return: the number of prime numbers.
    """
    def Count_PrimeNum(self, N):
        # 解题思路利用一个递推的思路，例如40 = 4*10 ,那么40的质数分解个数等于4的质数分解
        # 个数加上10的质数分解个数。开一个数组prime，prime[i]代表i的质数分解个数；
        # 当遍历到i时，所有小于等于i的prime值均已得到，故可得到所以i*j的prime值（1<j<i）复杂度分析
        #
        ans = 0
        vis = [False]*100005
        prime = [1]*100005
        for i in range(2,N+1):
            ans += prime[i]
            k = min(N//i,i)
            for j in range(2,k+1):
                if vis[i*j]:
                    continue
                vis[i*j] = True
                prime[i*j] = prime[i] + prime[j]
        return ans