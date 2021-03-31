'''
Given an array nums of integers, we need to find the maximum possible sum of 
elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4


'''
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        state = [0, float('-inf'), float('-inf')]

        for num in nums:
            if num % 3 == 0:
                state = [state[0] + num, state[1] + num, state[2] + num]
            if num % 3 == 1:
                a = max(state[2] + num, state[0])
                b = max(state[0] + num, state[1])
                c = max(state[1] + num, state[2])
                state = [a, b, c]
            if num % 3 == 2:
                a = max(state[1] + num, state[0])
                b = max(state[2] + num, state[1])
                c = max(state[0] + num, state[2])
                state = [a, b, c]
        return state[0]

    def maxSumDivThreeTotalSumSubstraction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones =  [float('inf')]*2
        twos =  [float('inf')]*2
        total = 0
        for i in nums:
            total += i
            if i % 3 == 1:
                if i < ones[0]: 
                    ones[1] = ones[0]
                    ones[0] = i
                elif i < ones[1]: ones[1] = i
            if i % 3 == 2:
                if i < twos[0]: 
                    twos[1] = twos[0]
                    twos[0] = i                    
                elif i < twos[1]: twos[1] = i
        #print(sorted(nums))
        #print(total, ones, twos)
        if total % 3 == 0: return total
        elif total % 3 == 1:
            if ones[0] > sum(twos): return total - sum(twos)
            return total - ones[0]
        elif total % 3 == 2:
            if twos[0] > sum(ones): return total - sum(ones)
            return total - twos[0]
        return 0

if __name__ == '__main__':
    nums = [366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]
    print(Solution().maxSumDivThreeTotalSumSubstraction(nums))

        
        