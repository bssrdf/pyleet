'''
-Medium-


Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of 
each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way 
to divide arr into 3 pairs each with sum divisible by 10.
Example 4:

Input: arr = [-10,10], k = 2
Output: true
Example 5:

Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true
 

Constraints:

arr.length == n
1 <= n <= 10^5
n is even.
-109 <= arr[i] <= 109
1 <= k <= 10^5

'''

from collections import defaultdict

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        """
        Keep count of remainders of all elements of arr
        frequency[0] keeps all elements divisible by k, and a divisible of k 
        can only form a group with other divisible of k. Hence, total number 
        of such divisibles must be even.
        for every element with remainder of i (i != 0) there should be a 
        element with remainder k-i.
        Hence, frequency[i] should be equal to frequency[k-i]
        """
        frequency = [0]*k
        for i in arr:
            frequency[i%k] += 1
        #print(frequency)
        if frequency[0]%2 != 0: return False
        for i in range(1, k//2+1):
            if frequency[i] != frequency[k-i]:
                return False
        return True

    def canArrangeAC(self, arr, k):
        n = len(arr)
        m = defaultdict(int)
        for i in arr:
            r = i % k
            d = 0 if r == 0 else k - r
            if d in m:
                m[d] -= 1
                if m[d] == 0: m.pop(d)
            else:
                m[r] += 1
        return not m
if __name__ == "__main__":
    print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5))
    print(Solution().canArrange([1,2,3,4,5,6], 10))
    print(Solution().canArrange([-1,1,-2,2,-3,3,-4,4],  3))
    print(Solution().canArrange([-1,-1,-1,-1,2,2,-2,-2], 3))
    print(Solution().canArrangeAC([1,2,3,4,5,10,6,7,8,9], 5))
    print(Solution().canArrangeAC([1,2,3,4,5,6], 10))
    print(Solution().canArrangeAC([-1,1,-2,2,-3,3,-4,4],  3))
    print(Solution().canArrangeAC([-1,-1,-1,-1,2,2,-2,-2], 3))