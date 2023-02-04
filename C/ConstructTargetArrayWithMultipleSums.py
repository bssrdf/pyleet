'''
-Medium-
*Priority Queue*
*Greedy*

Given an array of integers target. From a starting array, A consisting of all 1's, 
you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise 
return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true
 

Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9


'''
import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        A = target
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)

    def isPossible2(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        # 100%
        A = target
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        while total > 1 and -A[0] > total//2:
            a = -heapq.heappop(A)
            total -= a
            if total <= 1:
                return True if total == 1 else False
            a %= total
            total += a
            heapq.heappush(A, -a)
        return total == len(A)

if __name__ == "__main__":
    print(Solution().isPossible([9,3,5]))
    print(Solution().isPossible2([9,3,5]))