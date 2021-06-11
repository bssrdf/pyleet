'''
-Medium-
*Difference Array*

Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each 
element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]

'''


class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        df = [0]*(length+1)
        for i,j,k in updates:
            df[i] += k
            df[j+1] -= k
        ans = [0]*length
        ans[0] = df[0]
        for i in range(1,length):
            ans[i] = ans[i-1] + df[i]
        return ans 


if __name__ == "__main__":
    print(Solution().getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]))
