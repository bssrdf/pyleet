'''

-Medium-

Given the API rand7() that generates a uniform random integer in the range [1, 7], write a 

function rand10() that generates a uniform random integer in the range [1, 10]. You can only 
call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented 
function rand10() will be called while testing. Note that this is not an argument passed to rand10().

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
 

Example 1:

Input: n = 1
Output: [2]
Example 2:

Input: n = 2
Output: [2,8]
Example 3:

Input: n = 3
Output: [3,8,10]
 

Constraints:

1 <= n <= 105



'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        # 我们可以先凑出 rand10*N()，然后再通过 rand10*N() % 10 + 1 来获得 rand10()。那么，
        # 只需要将 rand7() 转化为 rand10*N() 即可，根据前面的讲解，我们转化也必须要保持等概率，
        # 那么就可以变化为 (rand7() - 1) * 7 + rand7()，就转为了 rand49()。但是 49 不是 10 的倍数，
        # 不过 49 包括好几个 10 的倍数，比如 40，30，20，10 等。这里，我们需要把 rand49() 转为 rand40()，
        # 需要用到 拒绝采样 Rejection Sampling，总感觉名字很奇怪，之前都没有听说过这个采样方法，刷题
        # 也是个不停学习新东西的过程呢。简单来说，这种采样方法就是随机到需要的数字就接受，不是需要的就拒绝，
        # 并重新采样，这样还能保持等概率，具体的证明这里就不讲解了，博主也不会，有兴趣的童鞋们可以去 Google 一下～ 
        # 这里直接用结论就好啦，当用  rand49() 生成一个 [1, 49] 范围内的随机数，如果其在 [1, 40] 范围内，
        # 我们就将其转为 rand10() 范围内的数字，直接对 10 去余并加1，返回即可。如果不是，则继续循环即可，

        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40: 
                return num % 10 + 1