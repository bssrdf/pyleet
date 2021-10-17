'''
-Hard-
*Two Pointers*
*Greedy*
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). 
A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 2 * 10^4
0 <= k < nums.length


'''

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A = nums
        res = mini = A[k]
        i, j, n = k, k, len(A)
        while i > 0 or j < n - 1:
            if (A[i - 1] if i else 0) < (A[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, A[i], A[j])
            res = max(res, mini * (j - i + 1))
        return res
        """
        l = r = k
        n = len(nums)
        res = 0
        mi = nums[k]
        while l >= 0 and r < n:
            print(mi, l, r, mi*(r-l+1))
            res = max(res, mi*(r-l+1))
            if l-1 >= 0 and r+1 < n:
                if nums[l-1] < nums[r+1]:
                    r += 1
                    mi = min(mi, nums[r])                    
                else:
                    l -= 1
                    mi = min(mi, nums[l])                    
            elif l-1 >= 0:
                l -= 1
                mi = min(mi, nums[l])                                
            elif r+1<n:
                r += 1
                mi = min(mi, nums[r])
        return res    
        """

    def maximumScoreMonoStack(self, heights, k):
        stack = []
        maxArea = 0
        heights.append(0)
        
        # stack saves the height in decreasing order
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                j = stack[-1] + 1 if stack else 0
                w = i - j
                # when it spans over k                     
                if j <= k and k <= i-1:
                    maxArea = max(maxArea, h * w)
            stack.append(i)

        i, j = k, k
        while i >= 0 and heights[i] >= heights[k]:
            i -= 1
        while j <= len(heights) and heights[j] >= heights[k]:
            j += 1
        maxArea = max(maxArea, heights[k] * (j - i - 1))
        
        return maxArea

    def maximumScoreMonoStack2(self, heights, k):
        stack = [-1]
        maxArea = 0
        #heights.append(0)
        n = len(heights)
        
        # stack saves the height in decreasing order
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                j = stack[-1] + 1 #if stack else 0
                w = i - j
                # when it spans over k
                if j <= k and k <= i-1:
                    maxArea = max(maxArea, h * w)
            stack.append(i)
        print(stack)
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = n-stack[-1]-1 
            if stack[-1] < k:
                maxArea = max(maxArea, h*w)
        
        return maxArea

    def maximumScoreMonoStack3(self, nums, k):
    
        n = len(nums)
        ans = 0 
        l, r = [-1]*n, [n]*n
        st = []  # find prev smaller and next smaller: mono increasing stack
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                r[st.pop()] = i #i's next greater
            if st: l[i] = st[-1]
            st.append(i)
        for i in range(n):
            if l[i] < k and r[i] > k:
                ans = max(ans, nums[i]*(r[i]-l[i]-1))
        return ans    

        

if __name__ == "__main__": 
    print(Solution().maximumScore(nums = [1,4,3,7,4,5], k = 3))
    print(Solution().maximumScoreMonoStack([1,4,3,7,4,5], 3))
    print(Solution().maximumScoreMonoStack2([1,4,3,7,4,5], 3))
    print(Solution().maximumScoreMonoStack3([1,4,3,7,4,5], 3))