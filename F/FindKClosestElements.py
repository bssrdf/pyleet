'''
-Medium-

Given a sorted integer array arr, two integers k and x, return the k closest 
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4


'''
import bisect
import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        idx = bisect.bisect_left(arr, x)
        l, r = idx-1, idx
        res = []
        while True:
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    ans = arr[l]
                    l -= 1
                else:
                    ans = arr[r]
                    r += 1
                res.append(ans)
            elif r < n:
                res.append(arr[r])
                r += 1
            else:
                res.append(arr[l])
                l -= 1    
            if len(res) == k: break
        return sorted(res)





if __name__ == "__main__":
    print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
    print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))