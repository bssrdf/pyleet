'''
-Medium-

Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
 

Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. 
Any permutation of [1,2,3] must be equally likely to be returned. 
Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original 
configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. 
Example: return [1, 3, 2]



Constraints:

1 <= nums.length <= 200
-10^6 <= nums[i] <= 10^6
All the elements of nums are unique.
At most 5 * 10^4 calls will be made to reset and shuffle.

'''
from random import randrange
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """        
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.nums[:]
        for i in range(self.n):
            # generate a random position t in [i,n-1]
            t = randrange(i, self.n)            
            # swap with number at t; t could be = i 
            res[i], res[t] = res[t], res[i]
        return res

        

if __name__ == "__main__":
# Your Solution object will be instantiated and called as such:
    obj = Solution([1, 2, 3])
    print(obj.shuffle())
    print(obj.reset())
    print(obj.shuffle())