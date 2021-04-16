'''
-Medium-
*DP*

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index 
position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly 
increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is 
guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].

'''

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        """
        swap[i] 表示范围 [0, i] 的子数组同时严格递增且当前位置i需要交换的最小交换次数，
        noSwap[i] 表示范围 [0, i] 的子数组同时严格递增且当前位置i不交换的最小交换次数
        """
        n = len(A)
        swap, noswap = [n] * n, [n] * n
        swap[0], noswap[0] = 1, 0
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1] and not (A[i] > B[i-1] and B[i] > A[i-1]):
                # the order is correct before the swap while incorrect after the swap -> should not swap
                # swap at i means also swapping at i-1
                # not swapping at i-1 violates the second half of the conditional
                swap[i] = swap[i-1] + 1
                # no need to swap
                noswap[i] = noswap[i-1]
            elif not (A[i] > A[i-1] and B[i] > B[i-1]) and (A[i] > B[i-1] and B[i] > A[i-1]):
                noswap[i] = swap[i-1] # we can achieve the goal by swapping at i-1, not at i
                swap[i] = noswap[i-1] + 1 # or swapping at i not at i-1
            else: # the order is correct no matter swap or not
                swap[i] = min(swap[i-1], noswap[i-1]) + 1 # can swap
                noswap[i] = min(noswap[i-1], swap[i-1])  # or not swap
        return min(swap[n-1], noswap[n-1])
    
if __name__ == "__main__":
    #print(Solution().minSwap(A = [1,3,5,4], B = [1,2,3,7]))
   #print(Solution().minSwap([3,3,8,9,10], [1,7,4,6,8]))
    print(Solution().minSwap([0,4,4,5,9], [0,1,6,8,10]))