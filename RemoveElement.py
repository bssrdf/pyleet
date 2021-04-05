# Time:  O(n)
# Space: O(1)
#
# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        
        l = 0
        r = len(A)
        while l < r:
            if A[l] == elem:              
                r -= 1
                A[l], A[r] = A[r], A[l]
            else:
                l += 1
       # print A
        return r
    
if __name__ == "__main__":
    print(Solution().removeElement([3, 3], 3))
    print(Solution().removeElement([4, 5], 4))
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2))
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 10))
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 5))
