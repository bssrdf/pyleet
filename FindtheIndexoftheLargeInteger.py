'''
-Medium-

We have an integer array arr, where all the integers in arr are equal except for one integer which 
is larger than the rest of the integers. You will not be given direct access to the array, 
instead, you will have an API ArrayReader which have the following functions:

int compareSub(int l, int r, int x, int y): where 0 <= l, r, x, y < ArrayReader.length(), l <= r and x <= y. 
The function compares the sum of sub-array arr[l..r] with the sum of the sub-array arr[x..y] and returns:
1 if arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y].
0 if arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y].
-1 if arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y].
int length(): Returns the size of the array.
You are allowed to call compareSub() 20 times at most. You can assume both functions work in O(1) time.

Return the index of the array arr which has the largest integer.

Follow-up:

What if there are two numbers in arr that are bigger than all other numbers?
What if there is one number that is bigger than other numbers and one number that 
is smaller than other numbers?
 

Example 1:

Input: arr = [7,7,7,7,10,7,7,7]
Output: 4
Explanation: The following calls to the API
reader.compareSub(0, 0, 1, 1) // returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with arr[1]).
Thus we know that arr[0] and arr[1] doesn't contain the largest element.
reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
Notice that we made only 3 calls, so the answer is valid.
Example 2:

Input: nums = [6,6,12]
Output: 2
 

Constraints:

2 <= arr.length <= 5 * 10^5
1 <= arr[i] <= 100
All elements of arr are equal except for one element which is larger than all other elements.
Hints
Do a binary search over the array, exclude the half of the array that doesn't contain the largest number.
Keep shrinking the search space till it reaches the size of 2 where you can easily determine which one has the largest integer.

'''

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l, r, x, y):
#        """
#        :type l, r, x, y: int
#        :rtype int
#        """
#
#	 # Returns the length of the array
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        '''
        The key is to figure out whether the array has odd or even number of elements. The rest is standard binary search.
        If we have odd number of elements, include mid.
        Sum of left array is 6 + 6 = 12, right array is 6 + 12 = 18.
        If we do not include mid, left sum and right sum would both be 12. We would get the wrong index.
        arr = [6,6,12]
                ^ include m
        If we have even number of elements, do not include mid.
        Sum of left array is 7 + 7 + 7 + 7 = 28, right array is 10 + 7 + 7 + 7 = 31. Obviously, the larger 
        element is on the right.
        arr = [7,7,7,7, | 10,7,7,7]
                        ^ split into two parts
        Time Complexity: O(logN), Space Complexity: O(N)
        Observation: the max possible length is 500_000, the log base 2 of 500_000 is 18.93 so we know 
        that we need to use binary search. Please see below the code with comments.*/
        '''
        l, r = 0, reader.length() - 1    
        while l < r :
            m = l + (r - l) // 2
            if (r - l) % 2 == 0:
                val = reader.compareSub(l, m, m, r)
            else:
                val = reader.compareSub(l, m, m + 1, r)
            if val == 1:
                r = m
            elif val == -1:
                l = m + 1
            elif val == 0:
                return m
        return l