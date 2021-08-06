'''
-Medium-

We have an integer array nums, where all the integers in nums are 0 or 1. You will not be 
given direct access to the array, instead, you will have an API ArrayReader which have the 
following functions:

int query(int a, int b, int c, int d): where 0 <= a < b < c < d < ArrayReader.length(). The 
function returns the distribution of the value of the 4 elements and returns:
4 : if the values of the 4 elements are the same (0 or 1).
2 : if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
0 : if two element have a value equal to 0 and two elements have a value equal to 1.
int length(): Returns the size of the array.
You are allowed to call query() 2 * n times at most where n is equal to ArrayReader.length().

Return any index of the most frequent value in nums, in case of tie, return -1.

Follow up: What is the minimum number of calls needed to find the majority element?

 

Example 1:

Input: nums = [0,0,1,0,1,1,1,1]
Output: 5
Explanation: The following calls to the API
reader.length() // returns 8 because there are 8 elements in the hidden array.
reader.query(0,1,2,3) // returns 2 this is a query that compares the elements nums[0], nums[1], nums[2], nums[3]
// Three elements have a value equal to 0 and one element has value equal to 1 or viceversa.
reader.query(4,5,6,7) // returns 4 because nums[4], nums[5], nums[6], nums[7] have the same value.
we can infer that the most frequent value is found in the last 4 elements.
Index 2, 4, 6, 7 is also a correct answer.
Example 2:

Input: nums = [0,0,1,1,0]
Output: 0
Example 3:

Input: nums = [1,0,1,0,1,0,1,0]
Output: -1
 

Constraints:

5 <= nums.length <= 10^5
0 <= nums[i] <= 1
Hints
If you find that 2 indexes in the array (id1, id2) have the same value 
(nums [id1] == nums [id2]), you could infer the values of (x, y) based on the 
results of query (id1, id2, x, y).

'''

# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """

from collections import Counter 
class ArrayReader(object):
    def __init__(self, nums): 
        self.nums = nums
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
    def query(self, a, b, c, d):
#        """
#        :type a, b, c, d: int
#        :rtype int
#        """
        tmp = [self.nums[a], self.nums[b], self.nums[c], self.nums[d]]
        C = Counter(tmp)
        if self.nums[a] == self.nums[b] and self.nums[b] == self.nums[c]   \
           and self.nums[c] == self.nums[d]:     
           return 4
        elif (1 in C and C[1] == 1) or (0 in C and C[0] == 1): return 2
        elif (1 in C and C[1] == 2) and (0 in C and C[0] == 2): return 0


#	 # Returns the length of the array
    def length(self):
        """
        :rtype int
        """       
        return len(self.nums)

class Solution(object):
    def guessMajority(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        n = reader.length()
        start = reader.query(0,1,2,3)
        g1, g2, idx1, idx2 = 1,  0,  0, -1
		# 假设idx = 0 的数是第一类，其个数为 g1 = 1
        for i in range(4, n):
            if reader.query(1,2,3,i) == start: # 0， i 是否是一类
                g1 += 1 
            else:
                g2 += 1; idx2 = i
        #0 与 4,5...n-1 是否是一类
        #还要确定1,2,3
        q = reader.query(0,2,3,4)
        p = reader.query(1,2,3,4)
        if q == p: #0和1是一类
            g1 += 1
        else:
            g2 += 1; idx2 = 1
        q = reader.query(0,1,3,4)
        # p = reader.query(1,2,3,4);
        if q == p: #0和2是否是一类
            g1 += 1 
        else:
            g2 += 1; idx2 = 2
        q = reader.query(0,1,2,4)
        # p = reader.query(1,2,3,4);
        if q == p: #0和3是否是一类
            g1 += 1
        else:
            g2 += 1; idx2 = 3
        if g1 == g2: return -1
        if g1 > g2: return idx1
        return idx2

if __name__ == "__main__":
    ar = ArrayReader([1,0,1,0,1,0,1,0])
    print(Solution().guessMajority(ar))
    ar = ArrayReader([0,0,1,0,1,1,1,1])
    print(Solution().guessMajority(ar))