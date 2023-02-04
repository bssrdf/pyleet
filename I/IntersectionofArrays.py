'''
-Medium-

Give a number of arrays, find their intersection, and output their intersection size.

The total number of all array elements is not more than 500000.
There are no duplicated elements in each array.
样例
Example 1:

	Input:  [[1,2,3],[3,4,5],[3,9,10]]
	Output:  1
	
	Explanation:
	Only '3' in all three array.
Example 2:

	Input: [[1,2,3,4],[1,2,5,6,7][9,10,1,5,2,3]]
	Output:  2
	
	Explanation:
	The set is [1,2].

'''

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        s = set(arrs[0])
        for arr in arrs[1:]:
            s = s & set(arr)
        return len(s)



if __name__ == "__main__":
    print(Solution().intersectionOfArrays([[1,2,3],[3,4,5],[3,9,10]]))
    print(Solution().intersectionOfArrays([[1,2,3,4],[1,2,5,6,7],[9,10,1,5,2,3]]))