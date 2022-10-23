'''

-Hard-

You are given two positive integer arrays nums and target, of the same length.

In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:

set nums[i] = nums[i] + 2 and
set nums[j] = nums[j] - 2.
Two arrays are considered to be similar if the frequency of each element is the same.

Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.

 

Example 1:

Input: nums = [8,12,6], target = [2,14,10]
Output: 2
Explanation: It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,5], target = [4,1,3]
Output: 1
Explanation: We can make nums similar to target in one operation:
- Choose i = 1 and j = 2, nums = [1,4,3].
Example 3:

Input: nums = [1,1,1,1,1], target = [1,1,1,1,1]
Output: 0
Explanation: The array nums is already similiar to target.
 

Constraints:

n == nums.length == target.length
1 <= n <= 105
1 <= nums[i], target[i] <= 106
It is possible to make nums similar to target.


'''

import tarfile
from typing import List
from collections import Counter
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        cnt1, cnt2 = Counter(nums), Counter(target)
        
        freq1_even = sorted([[c,f] for c,f in cnt1.items() if c%2 == 0 and (c not in cnt2 or f != cnt2[c])])
        freq1_odd  = sorted([[c,f] for c,f in cnt1.items() if c%2 == 1 and (c not in cnt2 or f != cnt2[c])])
        freq2_even = sorted([[c,f] for c,f in cnt2.items() if c%2 == 0 and (c not in cnt1 or f != cnt1[c])])
        freq2_odd  = sorted([[c,f] for c,f in cnt2.items() if c%2 == 1 and (c not in cnt1 or f != cnt1[c])])
        # freq2 = sorted([[c,f] for c,f in cnt2.items() if c not in cnt1 or f != cnt1[c]])
       

        # print(freq1_odd)
        # print(freq2_odd)
        # print(freq1_even)        
        # print(freq2_even)

        i, j = 0, 0
        pos, inc = 0, True
        ans = 0
        while i < len(freq1_odd) and j < len(freq2_odd):
            if pos == 0: inc = True
            else:
                inc = False
            a1, f1 = freq1_odd[i]
            a2, f2 = freq2_odd[j]            

            if f1 == f2: 
                pos += (a2-a1)*f2//2
                i += 1
                j += 1
            elif f1 < f2:
                pos += (a2-a1)*f1//2
                i += 1
                freq2_odd[j] = [a2, f2-f1]
            else:
                pos += (a2-a1)*f2//2
                j += 1
                freq1_odd[j] = [a1, f1-f2]                    
            if inc: ans += abs(pos) 
        # print('after odd', ans)
        i, j = 0, 0    
        pos = 0 
        while i < len(freq1_even) and j < len(freq2_even):
            if pos == 0: inc = True
            else:
                inc = False
            a1, f1 = freq1_even[i]
            a2, f2 = freq2_even[j]         
            if f1 == f2: 
                pos += (a2-a1)*f2//2
                i += 1
                j += 1
            elif f1 < f2:
                pos += (a2-a1)*f1//2
                i += 1
                freq2_even[j] = [a2, f2-f1]
            else:
                pos += (a2-a1)*f2//2
                j += 1
                freq1_even[j] = [a1, f1-f2]                    
            if inc: ans += abs(pos)                             

        return ans

    def makeSimilar2(self, nums: List[int], target: List[int]) -> int:
        cnt1, cnt2 = Counter(nums), Counter(target)
        
        # freq1_even = sorted([[c,f] for c,f in cnt1.items() if c%2 == 0 and (c not in cnt2 or f != cnt2[c])])
        # freq1_odd  = sorted([[c,f] for c,f in cnt1.items() if c%2 == 1 and (c not in cnt2 or f != cnt2[c])])
        # freq2_even = sorted([[c,f] for c,f in cnt2.items() if c%2 == 0 and (c not in cnt1 or f != cnt1[c])])
        # freq2_odd  = sorted([[c,f] for c,f in cnt2.items() if c%2 == 1 and (c not in cnt1 or f != cnt1[c])])
        freq1_even = sorted([[c,f] for c,f in cnt1.items() if c%2 == 0])
        freq1_odd  = sorted([[c,f] for c,f in cnt1.items() if c%2 == 1])
        freq2_even = sorted([[c,f] for c,f in cnt2.items() if c%2 == 0])
        freq2_odd  = sorted([[c,f] for c,f in cnt2.items() if c%2 == 1])
        print(freq1_odd)
        print(freq2_odd)
        print(freq1_even)        
        print(freq2_even)
        pos, neg = 0, 0
        i, j = 0, 0
        ans = 0
        
        while i < len(freq1_odd) and j < len(freq2_odd):
            pos, neg = 0, 0
            a1, f1 = freq1_odd[i]
            a2, f2 = freq2_odd[j]            
            if a1 < a2:    
                if f1 == f2: 
                    pos += (a2-a1)*f2//2
                    freq1_odd[i] = [a1, 0]
                    freq2_odd[j] = [a2, 0]
                    i += 1
                    j += 1                    
                elif f1 < f2:
                    pos += (a2-a1)*f1//2
                    freq1_odd[i] = [a1, 0]                    
                    i += 1
                    freq2_odd[j] = [a2, f2-f1]
                else:
                    pos += (a2-a1)*f2//2
                    freq2_odd[j] = [a2, 0]                    
                    j += 1
                    freq1_odd[i] = [a1, f1-f2]                    
                    
            else:
                if f1 == f2: 
                    neg += (a1-a2)*f2//2
                    freq1_odd[i] = [a1, 0]
                    freq2_odd[j] = [a2, 0]
                    i += 1
                    j += 1
                elif f1 < f2:
                    neg += (a1-a2)*f1//2
                    freq1_odd[i] = [a1, 0]
                    i += 1
                    freq2_odd[j] = [a2, f2-f1]
                else:
                    neg += (a1-a2)*f2//2
                    freq2_odd[j] = [a2, 0] 
                    j += 1
                    freq1_odd[i] = [a1, f1-f2]
            ans += max(pos, neg)  
            print(pos, neg, freq1_odd[i], freq2_odd[j],ans)


                    
        # ans = max(pos, neg)
        # print(i, len(freq1_odd),  j, len(freq2_odd))
        # print(freq1_odd)
        # print(freq2_odd)

        # pos1, neg1 = pos, neg
        # print(pos, neg)
        # pos, neg = 0, 0
        i, j = 0, 0
        while i < len(freq1_even) and j < len(freq2_even):
            
            a1, f1 = freq1_even[i]
            a2, f2 = freq2_even[j]  
            pos, neg = 0, 0          
            if a1 < a2:    
                if f1 == f2: 
                    pos += (a2-a1)*f2//2
                    freq1_even[i] = [a1, 0]
                    freq2_even[j] = [a2, 0]
                    i += 1
                    j += 1
                elif f1 < f2:
                    pos += (a2-a1)*f1//2
                    freq1_even[i] = [a1, 0]
                    i += 1
                    freq2_even[j] = [a2, f2-f1]
                else:
                    pos += (a2-a1)*f2//2
                    freq2_even[j] = [a2, 0]
                    j += 1
                    freq1_even[j] = [a1, f1-f2]                    
            else:
                if f1 == f2: 
                    neg += (a1-a2)*f2//2
                    freq1_even[i] = [a1, 0]
                    freq2_even[j] = [a2, 0]
                    i += 1
                    j += 1
                elif f1 < f2:
                    neg += (a1-a2)*f1//2
                    freq1_even[i] = [a1, 0]
                    i += 1
                    freq2_even[j] = [a2, f2-f1]
                else:
                    neg += (a1-a2)*f2//2
                    freq2_even[j] = [a2, 0]
                    j += 1
                    freq1_even[i] = [a1, f1-f2]
            ans += max(pos, neg)       
        # print(pos, neg)
        # print(pos-pos1, neg-neg1)
        # print(i, len(freq1_even),  j, len(freq2_even))
        # print(freq1_even)
        # print(freq2_even)
        # ans = max(pos, neg)
        return ans 

    def makeSimilar3(self, nums: List[int], target: List[int]) -> int:    
        onums = sorted([x for x in nums if x % 2])
        enums = sorted([x for x in nums if x % 2 == 0])
        otar = sorted([x for x in target if x % 2])
        etar = sorted([x for x in target if x % 2 == 0])
        return sum((x - y) // 2 for x, y in zip(onums, otar) if x > y) + \
               sum((x - y) // 2 for x, y in zip(enums, etar) if x > y)
    


if __name__ == "__main__":        
    # print(Solution().makeSimilar(nums = [8,12,6], target = [2,14,10]))
    # print(Solution().makeSimilar(nums = [1,2,5], target = [4,1,3]))
    # print(Solution().makeSimilar(nums = [1,1,1,1,1], target = [1,1,1,1,1]))
    # print(Solution().makeSimilar2(nums = [8,12,6], target = [2,14,10]))
    # print(Solution().makeSimilar2(nums = [1,2,5], target = [4,1,3]))
    # print(Solution().makeSimilar2(nums = [1,1,1,1,1], target = [1,1,1,1,1]))
    
    nums = [758,334,402,1792,1112,1436,1534,1702,1538,1427,720,1424,114,1604,564,120,578]
    target = [1670,216,1392,1828,1104,464,678,1134,644,1178,1150,1608,1799,1156,244,2,892]
    # print(Solution().makeSimilar(nums = nums, target=target))
    # print(Solution().makeSimilar2(nums = nums, target=target))
    nums = [4,634,1059,798,736,1102,1798,1198,1566,1293,165,1146,1314,1068,1555,448,839]
    target = [171,1775,1412,163,1004,854,716,1839,182,2000,696,1999,296,1152,478,306,1680]
    # print(Solution().makeSimilar2(nums = nums, target=target))

    nums = [369,691,379,191,333,595,187,800,161,97,436,488,505,313,89,943,91,875,672,71,854,936,570,813,363,987,359,269,439,899,961,112,986,848,792,775,13,298,490,715,541,967,964,179,767,278,845,223,305,603,407,745,260,533,795,629,609,53,781,365,782,674,525,985,55,940,525,753,805,659,642,593,911,871,556,517,863,839,767,291,723,676,213,650,627,716,373,55,889,437,507,950,615,13,417,109]
    target = [577,510,653,833,676,459,45,194,597,55,623,999,941,127,751,891,167,959,391,967,567,41,669,781,569,999,864,263,801,909,946,37,203,814,855,799,225,261,205,851,833,999,301,720,987,146,187,154,359,839,977,38,714,163,903,169,756,841,982,432,281,66,67,637,269,303,880,235,127,301,407,969,645,589,941,899,758,768,469,690,225,528,463,234,466,561,953,520,978,651,243,443,143,773,839,242]
    # print(Solution().makeSimilar2(nums = nums, target=target))

    nums = [44,590,100,354,524,144,898,943,968,266,856,294,553,494,369,907,623,169,1,352,465,209,561,600,415,591,4,254,55,932,344,484,638,260,740,806,21,590,187,631,326,829,4,770,664,251,849,814,912,143,158,476,16,82,401,276,306,151,444,172,760,165,384,906,346,456,10,210,712,622,230,629,254,97]
    target = [54,323,558,124,183,984,513,762,4,190,340,25,376,722,719,283,406,710,710,386,69,511,1,740,198,695,123,392,100,980,328,680,2,242,192,588,860,175,70,523,919,618,738,593,814,176,2,979,740,553,733,388,950,428,545,754,907,2,670,734,324,473,648,645,31,47,2,108,104,480,519,396,2,198]
    print(Solution().makeSimilar2(nums = nums, target=target))

        