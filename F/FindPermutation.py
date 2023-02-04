'''
-Medium-

A permutation perm of n integers of all the integers in the range [1, n] can be 
represented as a string s of length n - 1 where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the lexicographically smallest 
permutation perm and return it.

 

Example 1:

Input: s = "I"
Output: [1,2]
Explanation: [1,2] is the only legal permutation that can represented by s, 
where the number 1 and 2 construct an increasing relationship.
Example 2:

Input: s = "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can be represented as "DI", but 
since we want to find the smallest lexicographical permutation, you should return [2,1,3]
 

Constraints:

1 <= s.length <= 10^5
s[i] is either 'I' or 'D'.

'''

class Solution(object):    
    def findPermutation(self, s):
        # To obtain the lexicographically smallest permutation, always use the smallest 
        # possible integer at each index. If a “D” is met, count the maximum number of 
        # consecutive “D”s, and the numbers at such indices are permuted in descending 
        # order. Find the minimum possible number for the first “D”, and fill in all 
        # the indices with “D”. If an “I” is met, simply use the smallest number that 
        # is greater than the previous largest number.
        length = len(s)
        permutations = [0]*(length+1)
        curNum, startIndx, decreaseCount = 1, 0, 0
        for i in range(length):
            if s[i] == 'D':
                decreaseCount += 1
            else:
                if decreaseCount == 0:
                    permutations[i] = curNum
                    curNum += 1
                    startIndx += 1
                else:
                    num = curNum + decreaseCount
                    curNum = num + 1
                    for j in range(startIndx, i+1):
                        permutations[j] = num
                        num -= 1
                    startIndx = i + 1
                    decreaseCount = 0
        if decreaseCount == 0:
            permutations[length] = curNum
        else:
            num = curNum + decreaseCount
            curNum = num + 1
            for j in range(startIndx, length+1):
                permutations[j] = num
                num -= 1
        return permutations



if __name__ == "__main__":
    print(Solution().findPermutation("DI"))
    