'''
-Medium-
*Sorting*
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return 
any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000


'''

from typing import List
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        A = barcodes
        counter = Counter(A)
        print(counter)
        A.sort(reverse=True, key=lambda x: (counter[x],x))
        print(A)
        res = [0]*len(A)
        j = 0
        for i in range(0, len(A), 2):
            res[i] = A[j]
            j += 1
        for i in range(1, len(A), 2):
            res[i] = A[j]
            j += 1
        return res
        

if __name__ == "__main__":
    print(Solution().rearrangeBarcodes([1,1,1,2,2,2]))
    print(Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3]))
    print(Solution().rearrangeBarcodes([2,2,1,3]))
    print(Solution().rearrangeBarcodes([1,1,2]))
    print(Solution().rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8]))