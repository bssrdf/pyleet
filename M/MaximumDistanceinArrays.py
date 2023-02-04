'''
-Medium-
*Sorting*

Given m arrays, and each array is sorted in ascending order. Now you can pick up 
two integers from two different arrays (each array picks one) and calculate the distance. 
We define the distance between two integers a and b to be their absolute difference |a-b|. 
Your task is to find the maximum distance.

Example 1:

Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:

Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].

'''


class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    def maxDiff(self, arrs):
        # write your code here
        A, res = arrs, 0
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    res = max(res, max(abs(A[i][0]-A[j][-1]), abs(A[i][-1]-A[j][0])))
        return res
    
    def maxDiff2(self, arrs):
        # write your code here
        A = arrs
        nums = []  
        for i in range(len(A)):
            nums.append((A[i][0],i))
            nums.append((A[i][-1],i))
        nums.sort()
        if nums[0][1] == nums[-1][1]:            
            return max(abs(nums[0][0]-nums[-2][0]), abs(nums[1][0]-nums[-1][0]))
        return abs(nums[0][0]-nums[-1][0])    

            

if __name__ == "__main__":
    arrs =  [[1,2,3],
             [4,5],
             [1,2,3]]
    print(Solution().maxDiff(arrs))
    print(Solution().maxDiff2(arrs))
    arrs = [[1,2,3,4,5,6,7,8,9],[0,10]]
    print(Solution().maxDiff(arrs))
    print(Solution().maxDiff2(arrs))
