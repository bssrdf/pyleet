'''
-Medium-

*Monotonic Queue*

Given a circular array (the next element of the last element is the first element of 
the array), print the Next Greater Number for every element. The Next Greater Number 
of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't 
exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

'''

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)        
        st = []
        res = []         
        for i in range(2*n-1, -1, -1):
            # pretend iterating through nums+nums
            # use i%n to get actual element
            while st and nums[i%n] >= st[-1]:
                st.pop()
            if i <= n-1:   
                res.append(st[-1] if st else -1)            
            st.append(nums[i%n])        
        return list(reversed(res))

if __name__ == "__main__":
    print(Solution().nextGreaterElements([1,2,1]))