'''
-Medium-
*Greedy*
*Sort*
*Hash Table*

Given an array of integers arr of even length, return true if and only if it is possible to 
reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

 

Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false
 

Constraints:

0 <= arr.length <= 3 * 10^4
arr.length is even.
-10^5 <= arr[i] <= 10^5


'''
from collections import defaultdict

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        pos, neg, zeros = [], [], 0
        for i in range(n):
            if arr[i] == 0: zeros += 1
            elif arr[i] > 0: pos.append(arr[i])
            else: neg.append(arr[i])
        if zeros % 2: return False
        if len(neg) % 2 or len(pos) % 2: 
            return False
        neg.sort(reverse=True)
        pos.sort()
        def check(A):
            s = defaultdict(int)
            for i in A:            
                if i % 2 == 0:
                    k = i // 2
                    if k in s:
                        s[k] -= 1
                        if s[k] == 0:
                            s.pop(k)
                        continue
                s[i] += 1            
            if s: return False            
            return True                           
        return check(pos) and check(neg)

    
        
        



if __name__ == "__main__":
    print(Solution().canReorderDoubled([4,-2,2,-4]))
    print(Solution().canReorderDoubled([3,1,3,6]))
    print(Solution().canReorderDoubled([2,1,2,6]))
    print(Solution().canReorderDoubled([1,2,4,16,8,4]))
    print(Solution().canReorderDoubled([1,2,4,8]))
    print(Solution().canReorderDoubled([2,1,2,1,1,1,2,2]))
    a = [7,-15,-15,23,-3,80,-35,40,68,22,44,98,20,0,-34,8,40,41,16,46,16,49,-6,-11,35,-15,-74,72,-8,60,40,-2,0,-6,34,14,-16,-92,54,14,-68,82,-30,50,22,25,16,70,-1,-96,11,45,54,40,92,-35,29,80,46,-30,27,7,-70,-37,41,-46,-98,1,-33,-24,-86,-70,80,-43,98,-49,30,0,27,2,82,36,0,-48,3,-100,58,32,90,-22,-50,-12,36,6,-3,-66,72,8,49,-30]
    print(Solution().canReorderDoubled(a))

