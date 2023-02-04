'''
-Easy-

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?

Use two pointers, see 2nd solution

What if nums1's size is small compared to nums2's size? Which algorithm is better?

What if elements of nums2 are stored on disk, and the memory is limited such that 
you cannot load all elements into the memory at once?

如果只有nums2不能放在内存中，则将nums1做成哈希表，nums2分批加载到内存中处理。
(If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, 
read chunks of array that fit into the memory, and record the intersections.)

如果nums1和nums2都很大，都不适合储存在内存，那么就用外部排序分别来sort它们。
将每2G(举例)读入内存，使用2指针技术，然后从内存中读取更多的2G。重复此操作，直到没有
更多数据从磁盘读取。(If both nums1 and nums2 are so huge that neither fit into 
the memory, sort them using external sort, read (let’s say) 2G of each into 
memory and then using the 2 pointer technique, then read 2G more from the 
array that has been exhausted. Repeat this until no more data to read from disk.)

还有一种思路是将这两个字符串存放在分布式系统中（不管是否自设计），然后使用MapReduce技
术来解决问题。

'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        res = []
        for i in nums1:
            m[i] = m.setdefault(i,0)+1            
        for i in nums2:
            if i in m and m[i] > 0:
                res.append(i)
                m[i] -= 1
        return res

    def intersectSort(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]: 
                res.append(nums1[i])            
                i += 1; j += 1
            elif nums1[i] > nums2[j]: j += 1
            else: i += 1
        return res


if __name__ == "__main__":
    print(Solution().intersect([1,2,2,1], [2,2]))
    print(Solution().intersectSort([1,2,2,1], [2,2]))
    print(Solution().intersectSort([4,9,5], [9,4,9,8,4]))