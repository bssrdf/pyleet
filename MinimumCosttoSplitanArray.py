'''

-Hard-
*DP*

You are given an integer array nums and an integer k.

Split the array into some number of non-empty subarrays. The cost of a split is the sum of the importance value of each subarray in the split.

Let trimmed(subarray) be the version of the subarray where all numbers which appear only once are removed.

For example, trimmed([3,1,2,4,3,4]) = [3,4,3,4].
The importance value of a subarray is k + trimmed(subarray).length.

For example, if a subarray is [1,2,3,3,3,4,4], then trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4].The importance value of this subarray will be k + 5.
Return the minimum possible cost of a split of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1,2,1,3,3], k = 2
Output: 8
Explanation: We split nums to have two subarrays: [1,2], [1,2,1,3,3].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1,3,3] is 2 + (2 + 2) = 6.
The cost of the split is 2 + 6 = 8. It can be shown that this is the minimum possible cost among all the possible splits.
Example 2:

Input: nums = [1,2,1,2,1], k = 2
Output: 6
Explanation: We split nums to have two subarrays: [1,2], [1,2,1].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1] is 2 + (2) = 4.
The cost of the split is 2 + 4 = 6. It can be shown that this is the minimum possible cost among all the possible splits.
Example 3:

Input: nums = [1,2,1,2,1], k = 5
Output: 10
Explanation: We split nums to have one subarray: [1,2,1,2,1].
The importance value of [1,2,1,2,1] is 5 + (3 + 2) = 10.
The cost of the split is 10. It can be shown that this is the minimum possible cost among all the possible splits.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
1 <= k <= 109



'''

from typing import List
from math import inf
from collections import Counter

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf]*(n+1)
        dp[0] = 0
        imp = {}
        for l in range(1, n+1):
            uni, mul = set(), Counter()
            for i in range(n):
                if nums[i] in uni:
                    uni.remove(nums[i])
                    mul[nums[i]] = 2 
                elif nums[i] not in mul:
                    uni.add(nums[i])
                else:
                    mul[nums[i]] += 1
                if i >= l:
                    j = i-l
                    if nums[j] in uni:
                        uni.remove(nums[j])
                    else: 
                        mul[nums[j]] -= 1
                        if mul[nums[j]] == 1:
                            uni.add(nums[j])
                            mul.pop(nums[j])
                if i >= l-1:
                    imp[(i-l+1, i+1)] = k + l - len(uni)
        # print(len(imp))
        for i in range(1,n+1):
            for j in range(i):
                dp[i] = min(dp[i], dp[j]+imp[(j, i)])
        return dp[n]        
    
    def minCost2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf]*(n+1)
        dp[0] = 0
        imp = [[0]*(n+1) for _ in range(n+1)]
        for l in range(1, n+1):
            uni, mul = set(), Counter()
            for i in range(n):
                if nums[i] in uni:
                    uni.remove(nums[i])
                    mul[nums[i]] = 2 
                elif nums[i] not in mul:
                    uni.add(nums[i])
                else:
                    mul[nums[i]] += 1
                if i >= l:
                    j = i-l
                    if nums[j] in uni:
                        uni.remove(nums[j])
                    else: 
                        mul[nums[j]] -= 1
                        if mul[nums[j]] == 1:
                            uni.add(nums[j])
                            mul.pop(nums[j])
                if i >= l-1:
                    imp[i-l+1][i+1] = k + l - len(uni)
        for i in range(1,n+1):
            for j in range(i):
                dp[i] = min(dp[i], dp[j]+imp[j][i])
        return dp[n]        
    
    def minCost3(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf]*(n+1)
        dp[0] = 0
        imp = [[k]*(n+1) for _ in range(n+1)]
        # for r in range(n, 0, -1):
        for r in range(1, n+1):
            mul = Counter()
            for l in range(r-1, -1, -1):
                if nums[l] not in mul:
                    imp[l][r] = imp[l+1][r]
                elif mul[nums[l]] == 1:
                    imp[l][r] = imp[l+1][r] + 2                    
                else:
                    imp[l][r] = imp[l+1][r] + 1                    
                mul[nums[l]] += 1  
                # if r == n:
                #     print(r, l, imp[l][r], mul)
        # for row in imp:
        #     print(row)              
        for i in range(1,n+1):
            for j in range(i):
                dp[i] = min(dp[i], dp[j]+imp[j][i])
        return dp[n]        
    

    def minCost4(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf]*(n+1)
        dp[0] = 0
        for r in range(1,n+1):
            mul = Counter()
            imp0 = k
            for l in range(r-1, -1, -1):
                if nums[l] not in mul:
                    imp = imp0
                elif mul[nums[l]] == 1:
                    imp = imp0 + 2                    
                else:
                    imp = imp0 + 1                    
                mul[nums[l]] += 1  
                dp[r] = min(dp[r], dp[l]+imp)
                imp, imp0 = imp0, imp
        return dp[n]        
    
    def minCost5(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf]*(n+1)
        dp[0] = 0
        for r in range(1,n+1):
            mul = Counter()
            imp = 0
            for l in range(r-1, -1, -1):                                
                imp += mul[nums[l]] > 0
                imp += mul[nums[l]] == 1                    
                mul[nums[l]] += 1  
                dp[r] = min(dp[r], dp[l]+imp+k)
        return dp[n]        



if __name__ == '__main__':
    print(Solution().minCost(nums = [1,2,1,2,1,3,3], k = 2)) 
    print(Solution().minCost(nums = [1,2,1,2,1], k = 2)) 
    print(Solution().minCost(nums = [1,2,1,2,1], k = 5)) 
    print(Solution().minCost2(nums = [1,2,1,2,1,3,3], k = 2)) 
    print(Solution().minCost2(nums = [1,2,1,2,1], k = 2)) 
    print(Solution().minCost2(nums = [1,2,1,2,1], k = 5)) 
    print(Solution().minCost3(nums = [1,2,1,2,1,3,3], k = 2)) 
    print(Solution().minCost4(nums = [1,2,1,2,1,3,3], k = 2)) 
    nums = [56,3,34,72,46,54,46,22,15,58,61,85,49,52,23,41,31,36,66,75,3,24,46,4,49,33,53,31,87,65,54,24,29,8,13,24,3,43,29,38,73,74,4,60,76,53,76,89,36,86,57,73,83,5,11,90,53,18,28,0,68,15,71,48,40,78,30,78,25,82,9,42,63,82,18,4,84,18,87,61,18,56,12,81,62,0,84,45,90,76,90,26,68,9,60,60,57,2,89,81,48,88,12,89,32,19,60,27,39,8,32,67,63,10,41,49,44,83,56,82,63,54,22,54,11,11,79,66,87,55,43,85,18,54,81,50,20,69,76,29,86,26,34,0,13,81,56,23,53,13,37,26,47,30,19,60,53,3,31,38,35,57,70,11,86,70,45,19,22,73,80,17,16,30,31,39,51,78,39,85,75,53,12,36,13,11,30,75,73,71,5,45,0,14,60,17,67,17,8,30,85,90,37,7,20,65,85,18,1,8,84,31,0,17,5,70,43,56,52,21,88,45,40,14,34,75,57,49,87,50,49,64,28,24,41,43,53,73,6,54,66,83,58,58,72,73,17,40,27,63,28,34,37,87,59,56,57,21,80,37,57,87,90,48,34,41,20,44,44,79,17,44,46,60,67,84,30,37,40,77,59,24,48,11,86,36,15,18,67,48,89,12,9,4,79,61,10,86,50,21,55,15,7,44,73,20,55,20,16,16,32,7,18,10,64,24,81,81,62,27,5,29,54,8,21,47,4,83,62,57,54,37,32,51,70,20,69,86,26,38,57,58,44,28,23,36,55,50,88,71,23,63,54,81,59,34,0,72,50,63,14,12,47,45,33,27,78,82,66,74,3,46,3,34,60,15,83,61,29,52,15,33,3,5,50,3,66,9,56,45,6,65,6,61,22,46,8,38,4,73,81,74,23,67,63,45,76,24,26,61,26,31,85,74,36,89,52,63,30,55,30,18,88,42,37,43,52,55,8,36,89,20,11,6,80,13,58,44,61,34,58,59,84,52,43,43,57,58,18,26,32,36,45,52,54,81,42,76,88,49,23,52,79,86,64,80,4,42,88,68,89,87,21,57,4,59,79,68,72,8,43,73,69,64,64,57,83,73,62,46,29,57,13,57,49,66,51,50,30,53,15,70,54,67,74,9,55,22,13,60,71,79,17,73,8,76,68,12,85,53,20,4,69,49,10,17,28,65,87,72,19,27,46,74,25,47,90,7,1,15,64,77,58,24,2,48,90,23,54,9,36,20,21,60,85,16,11,88,43,8,54,19,77,73,61,65,73,67,21,49,18,14,2,40,89,32,74,32,24,32,55,20,49,63,81,42,17,88,86,54,88,53,54,52,67,48,71,53,53,26,16,39,66,62,64,90,17,62,73,49,13,48,67,76,60,0,20,70,29,81,89,45,39,11,79,83,25,43,17,16,76,66,61,41,85,18,20,73,39,77,2,36,10,43,2,82,49,47,39,1,73,69,72,90,20,73,1,26,34,25,50,64,73,28,77,3,86,12,86,13,46,29,3,64,77,3,6,61,87,2,30,68,80,36,50,28,34,74,73,14,70,55,65,81,83,44,5,20,9,63,2,46,27,20,79,59,90,14,34,49,2,7,89,0,39,22,52,67,51,16,5,44,42,87,73,1,20,74,70,50,47,4,60,36,12,33,61,47,55,14,58,90,84,26,90,57,71,25,69,87,22,13,20,87,2,75,58,58,39,13,86,12,0,76,67,3,36,27,44,21,7,75,34,15,39,62,23,82,8,43,62,77,90,65,73,77,27,62,1,28,33,64,83,48,67,69,89,54,24,43,38,64,59,30,89,77,61,48,78,61,80,37,66,49,39,36,73,60,35,24,59,11,39,70,54,70,44,42,70,82,19,38,89,11,11,36,58,75,30,14,13,10,53,88,86,61,84,68,52,62,53,62,71,61,68,0,38,83,6,31,35,26,62,20,6,74,21,44,15,72,55,80,74,57,17,75,73,61,65,33,66,80,74,49,73,9,45,54,62,43,35,54,71,63,49,84,22,42,71,2,75,0,22,64,28,28]
    print(Solution().minCost(nums = nums , k = 8)) 
    print(Solution().minCost2(nums = nums , k = 8)) 
    print(Solution().minCost3(nums = nums , k = 8)) 
    print(Solution().minCost5(nums = nums , k = 8)) 
    nums = [173,836,592,162,939,495,398,314,433,175,673,639,461,695,491,975,91,14,898,406,867,180,816,479,617,16,674,561,307,954,440,437,105,495,385,489,433,268,214,851,672,831,705,44,996,825,899,407,9,105,817,849,131,139,154,144,493,226,993,221,49,957,909,298,260,250,929,467,597,805,639,79,815,809,50,160,280,599,735,872,487,54,565,676,52,312,923,470,858,983,664,262,432,629,413,995,394,274,43,214,698,262,654,606,539,519,844,381,197,456,14,53,672,122,984,397,334,529,84,800,5,941,691,311,29,298,865,830,856,638,436,827,539,153,136,623,649,95,142,389,477,832,143,354,295,345,255,727,873,824,31,86,493,954,133,57,203,662,121,960,353,85,827,866,995,520,769,233,473,334,690,146,71,918,493,410,194,135,512,771,385,190,546,784,150,93,762,134,541,316,550,71,657,794,531,62,170,937,947,795,876,885,457,794,693,467,499,664,102,53,921,795,291,361,641,6,786,657,549,315,803,402,90,864,846,489,855,300,586,694,0,778,992,138,868,89,977,239,698,364,144,493,137,581,133,725,173,694,354,352,689,836,784,703,20,760,195,673,65,525,485,17,443,720,819,506,245,640,77,754,188,780,236,310,60,260,770,570,739,165,945,365,973,212,262,406,956,269,255,903,24,861,5,819,104,39,748,309,960,568,716,162,857,321,188,568,7,768,764,97,309,263,620,575,256,104,226,495,573,520,597,592,397,770,390,402,246,479,441,666,243,85,378,124,915,255,931,353,162,479,185,482,195,701,528,147,358,251,600,11,947,288,803,660,97,268,620,520,551,362,994,323,112,327,612,363,815,782,87,202,24,111,473,233,14,126,286,240,743,402,502,186,358,847,495,121,552,183,28,45,981,254,552,810,364,450,895,421,775,560,671,753,792,558,271,632,985,682,678,310,413,108,614,898,769,191,155,923,586,526,492,646,548,777,816,735,683,827,156,50,574,152,164,573,143,690,292,502,723,805,740,400,680,803,735,461,712,960,680,155,918,247,814,350,431,42,408,798,911,884,406,492,769,347,442,809,146,361,416,247,223,784,703,106,212,623,414,265,355,606,409,995,482,132,753,283,389,525,140,819,437,687,679,139,930,382,394,880,565,332,278,390,743,835,962,556,753,529,490,370,74,390,794,895,960,930,725,701,165,926,35,208,658,247,909,917,773,788,652,754,578,363,438,368,341,112,184,726,555,340,709,532,745,961,498,448,208,516,459,500,837,257,933,852,660,849,496,627,112,421,204,190,447,955,339,324,192,125,256,652,351,86,285,861,507,85,591,709,613,131,198,539,136,771,546,928,875,108,858,461,430,794,632,792,43,152,265,91,525,815,760,210,92,20,23,157,673,549,84,832,973,467,948,123,418,497,901,103,942,171,571,947,731,610,512,721,340,754,588,258,494,468,547,19,763,173,637,696,742,52,817,338,677,334,832,187,742,209,449,408,358,670,362,6,98,930,796,651,130,575,764,26,737,637,197,18,517,476,598,515,840,272,573,360,216,382,922,0,196,815,483,511,538,417,541,658,242,265,863,27,290,352,254,390,970,920,75,297,810,119,512,150,987,363,922,56,465,844,364,246,193,958,475,918,980,555,148,445,707,426,798,51,260,601,395,370,679,423,495,983,87,609,823,99,180,961,703,271,522,918,514,991,436,87,508,183,322,758,284,619,693,902,63,525,225,382,362,462,204,203,226,100,701,603,750,135,104,940,899,524,759,366,525,8,497,810,692,541,470,638,281,333,614,709,467,87,528,778,165,915,508,531,892,689,405,140,615,923,520,124,156,692,353,470,46,679,64,761,940,596,409,668,503,360,803,993,916,838,186,45,481,859,549,345,626,840,198,722,672,194,10,222,541,690,817,68,114,830,459,401,659,496,317,821,200,647,566,798,872,316,523,860,457,896,386,729,577,159,823,3,314,348,424,709,459,571,674,266,144,587,462,782,691,424,336,580,135,730,353,418,461,797,639,685,684,20,843,48,61,552,609,943,583,340,576,760,758,228,885,854,419,153,676,965,359,536,767,646,542,262,670,408,711,35,537,995,887,400,476,177,782,178,656,9,870,214,936,261,123,458,791,490,636,5,469,507,882,426,312,970,811,801,324,320,566,666,865,313,861,843,575,668,84,357,774,229,568,884,99,118,849,212,853,602,998,51,43,593,905,833,353,737,927,260,95,556,112,417,522,448,500,813,394,996,476,709,646,560,305,558,762,576,644,682,781,285,951,40,295,820]    
    print(Solution().minCost5(nums = nums , k = 999999913)) 