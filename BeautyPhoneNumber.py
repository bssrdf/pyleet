'''
-Medium-

链接：https://www.nowcoder.com/questionTerminal/005af31a10834b3688911463065ab47d
来源：牛客网

A 国的手机号码由且仅由 N 位十进制数字(0-9)组成。一个手机号码中有至少 K 位数字相同则被定义为靓号。
A 国的手机号可以有前导零，比如 000123456 是一个合法的手机号。
小多想花钱将自己的手机号码修改为一个靓号。修改号码中的一个数字需要花费的金额为新数字与旧数字之间
的差值。比如将 1 修改为 6 或 6 修改为 1 都需要花 5 块钱。
给出小多现在的手机号码，问将其修改成一个靓号，最少需要多少钱？

输入描述:
第一行包含2个整数 N、K，分别表示手机号码数字个数以及靓号至少有 K 个数字相同。
第二行包含 N 个字符，每个字符都是一个数字('0'-'9')，数字之间没有任何其他空白符。表示小多的
手机号码。
数据范围：
2 <= K <= N <= 10000


输出描述:
第一行包含一个整数，表示修改成一个靓号，最少需要的金额。
第二行包含 N 个数字字符，表示最少花费修改的新手机号。若有多个靓号花费都最少，则输出字典序最小的靓号。
示例1
输入
6 5
787585
输出
4
777577
说明
花费为4的方案有两种：777577与777775，前者字典序更小。

'''


from collections import Counter
class Solution(object):
    def pickNumber(self, s, k):       
        
        d = Counter(list(map(int,s)))
        res = float("inf")
        ans = "A"
        for i in range(10):
            tmp_s = s
            need = k - d[i]
            cost = 0
            gap = 1
            while need > 0:
                if i+gap <= 9:
                    if d[i+gap] < need:
                        tmp_s = tmp_s.replace(str(i + gap), str(i))
                        cost += d[i+gap] * gap
                        need -= d[i+gap]
                    else:
                        tmp_s = tmp_s.replace(str(i + gap), str(i), need)
                        cost += need * gap
                        break
                if i - gap >= 0:
                    if d[i-gap] < need:
                        tmp_s = tmp_s.replace(str(i-gap), str(i))
                        cost += d[i-gap] * gap
                        need -= d[i-gap]
                    else:
                        tmp_s = tmp_s[::-1]
                        tmp_s = tmp_s.replace(str(i-gap), str(i), need)
                        tmp_s = tmp_s[::-1]
                        cost += need * gap
                        break
                gap += 1
            if cost < res:
                ans = tmp_s
                res = cost
            elif cost == res and  tmp_s < ans:
                ans = tmp_s
        return ans

if __name__ == "__main__": 

    print(Solution().pickNumber('787585',5))