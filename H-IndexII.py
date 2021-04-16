'''
-Medium-

Given an array of integers citations where citations[i] is the number of citations a researcher 
received for their ith paper and citations is sorted in an ascending order, return compute 
the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their 
n papers have at least h citations each, and the other n − h papers have no more than h 
citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

 

Example 1:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,2,100]
Output: 2
 

Constraints:

n == citations.length
1 <= n <= 10^5
0 <= citations[i] <= 1000
citations is sorted in ascending order.


Follow up: Could you solve it in logarithmic time complexity?
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """
        To understand this we should have a clear understanding of the origin solution to this problem. 
        It is on wikipage: https://en.wikipedia.org/wiki/H-index

        Summary here:
        Sort the array descending order, give each a index start from 1.
        From right to left, find the last number >= its index, the result is its index.

        ....c: 25, 8, 5, 3, 3
        index:1, 2, 3, 4, 5
        number 5, H-index 3.

        After understand this origin solution, we can go to the binary search one.
        First, the different is the order changed, in this problem, the array sorted in ascending.
        We need somehow transfer it to original problem.

        For example, we have those number, and their index starts with 0
        ......c: 3, 3, 5, 8, 25　
        index: 0, 1, 2, 3, 4

        We can covert it using n the length of the array. We subtract n with the index, we get:
        ........c: 3, 3, 5, 8, 25　
        index0: 0, 1, 2, 3, 4　
        index1: 5, 4, 3, 2, 1

        We can see we almost have the original form now except the order. It is easy, in the original 
        problem we try to find the last one >= its index, now we find the first one >= its index.

        So now we just using binary search to find the number, a thing here we need to mind is the 
        index0 here we are using, but we need to convert it to index1.
        """
        n = len(citations)
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            # recast index i from [0, 1, ....n-1] to j [n, n-1, ... 1]
            # by doing j = n-i
            # search for the first recasted index j where c[j] >= j 
            if citations[m] < n - m:
                l = m + 1
            else:
                r = m
        return n - l 


if __name__ == "__main__":
     print(Solution().hIndex([0,1,3,5,6]))