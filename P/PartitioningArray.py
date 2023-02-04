'''
-Easy-

Given an array of numbers, you are required to check if it is possible to partition the array into some 
subsequences of length k each, such that:

Each element in the array occurs in exactly one subsquence
All the numbers in a subsequence are distinct
Elements in the array having the same value must be in different subsequences
Is possible to partition the array satisfying the above conditions? If it is possible, return true, else return false.

样例
Example1:
Input:
A:[1, 2, 3, 4]
k = 2
output: true
Explanation:
Then one possible way is to choose the first 2 elements of the array {1, 2} as the first subsequence, the next 2 elements {3, 4} as the next subsquence.So the answer is true
Example2:
Input:
A: [1, 2, 2, 3]
k: 3
output: false
Explanation:
there is no way to partition the array into subsequences such that all subsquences are of length 3 and each element in the array occurs in exactly one subsequece.Hence the answer is false.


'''
from collections import Counter

class Solution:
    """
    @param A: Integer array
    @param k: a integer
    @return: return is possible to partition the array satisfying the above conditions
    """
    def PartitioningArray(self, A, k):
        # write your code here        
        if len(A) % k != 0: return False
        m = Counter(A)
        return max(m.values(),default=1) <= k 

        
         


    
if __name__=="__main__":
    print(Solution().PartitioningArray([1, 2, 3, 4], 2))
    print(Solution().PartitioningArray([1, 2, 2, 3], 3))
    print(Solution().PartitioningArray([], 1))