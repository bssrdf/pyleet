'''
-Medium-

Given two integer arrays nums1 and nums2, return the maximum length of a subarray 
that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100


'''

class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1]+1 if nums1[i-1] == nums2[j-1] else 0
                res = max(res, dp[i][j])
        return res

    def findLengthONSpace(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [0]*(n+1)
        res = 0
        for i in range(m-1, -1, -1):
            for j in range(n):
                dp[j] = dp[j+1]+1 if nums1[i] == nums2[j] else 0
                res = max(res, dp[j])
        return res
    
    def findLengthBinarySearchHash(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 99%, 82%
        # we can convert to string like below because 0 <= nums[i] < 100;
        str1, str2 = ''.join([chr(x) for x in nums1]), ''.join([chr(x) for x in nums2])
        m, n = len(str1), len(str2)
        left, right = 0, min(m,n)+1

        def helper(s1, s2, lth):
            st = set()
            for i in range(m-lth+1):
                st.add(s1[i:i+lth])
            for j in range(n-lth+1):
                if s2[j:j+lth] in st: 
                  #  print('found:',s2[j:j+lth], lth)
                    return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if helper(str1, str2, mid): left = mid + 1
            else: right = mid
            print(left, right, mid)
        #print(left, right)
        return right - 1




  
if __name__ == "__main__":
    '''
    final dp array 
      x 1 2 3 2 1
    x 0 0 0 0 0 0
    3 0 0 0 1 0 0
    2 0 0 1 0 2 0 
    1 0 1 0 0 0 3  
    4 0 0 0 0 0 0 
    7 0 0 0 0 0 0 
    '''
    '''
    print(Solution().findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7])) 
    print(Solution().findLengthONSpace(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))  
    print(Solution().findLengthBinarySearchHash(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))  
    print(Solution().findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))  
    print(Solution().findLengthONSpace(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))   
    print(Solution().findLengthBinarySearchHash(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))
    '''  
    print(Solution().findLengthBinarySearchHash([70,39,25,40,7],[52,20,67,5,31]))     