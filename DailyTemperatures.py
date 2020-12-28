'''
-Medium-

*Monotonic Queue*

Given a list of daily temperatures T, return a list such that, for each day in the 
input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature 
will be an integer in the range [30, 100].

'''

class Solution(object):
    
    def dailyTemperaturesFast(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
           while stack and T[stack[-1]] < t:
              cur = stack.pop()
              ans[cur] = i - cur
           stack.append(i)
        return ans

    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        st = []
        res = []        
        for i in range(len(T)-1, -1,-1):
            while st and T[i] >= T[st[-1]]:
                st.pop()
            if not st:
                res.append(0)
            else:
                res.append(st[-1]-i)
            # save index into the stack
            st.append(i)
        return list(reversed(res))

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))