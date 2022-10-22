'''

-Medium-

We have an array arr of non-negative integers.

For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].

Return the number of possible results. Results that occur more than once are only counted once in the final answer

 

Example 1:

Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.
Example 2:

Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 109



'''

from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # wrong solution
        n = len(arr)
        st = set()
        pos = [-1]*31
        ans = 0
        mask = 0
        for i, a in enumerate(arr):
            print(f'{a:08b}')
            for j in range(31):
                if a & (1<<j) > 0:
                    pos[j] = i
            p = i
            for j in range(31):
                if pos[j] != -1:
                    p = min(p, pos[j])
            ans += (i-p)
            if a not in st:
                ans += 1
            mask |= a
            st.add(mask)

        return ans   
    
    def subarrayBitwiseORs2(self, arr: List[int]) -> int:
        A = arr
        res, cur = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)


if __name__ == "__main__":
    print(Solution().subarrayBitwiseORs(arr = [0]))
    print(Solution().subarrayBitwiseORs(arr = [1,1,2]))
    print(Solution().subarrayBitwiseORs(arr = [1,2,4]))
    print(Solution().subarrayBitwiseORs(arr = [9, 6, 15]))
    print(Solution().subarrayBitwiseORs(arr = [13, 4, 2]))

    print(Solution().subarrayBitwiseORs2(arr = [0]))
    print(Solution().subarrayBitwiseORs2(arr = [1,1,2]))
    print(Solution().subarrayBitwiseORs2(arr = [1,2,4]))
    print(Solution().subarrayBitwiseORs2(arr = [9, 6, 15]))
    print(Solution().subarrayBitwiseORs2(arr = [13, 4, 2]))
     