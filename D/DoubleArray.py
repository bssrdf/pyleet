'''
-Easy-

Given an array of positive integers arr and a positive integer num.
While iterating through the array arr, num will double if its equal to the current element.
Please rearrange array arr to maximize num.

1 <= N <= 10^5

 
1 <= num <= 10^8
 

样例
Example 1:

Input:

arr = [1,2,1,3,2]
num = 1
Output:

4
Explanation:

You can rerange this array as [1,2,3,1,2], then traverse this array:
because of a[0] = 1 and num == a[0], so num = num * 2 = 2,
because of a[1] = 2 and num == a[1], so num = num * 2 = 4,
because of a[2] = 3 and num != a[2], so num does not change,
because of a[3] = 1 and num != a[3], so num does not change,
because of a[4] = 2 and num != a[4], so num does not change.
You can also rerange this array as [1,2,1,2,3], and you will get num = 4 as well.

'''

class Solution:
    """
    @param arr: a positive integer array
    @param num: a positive integer
    @return: return the maxium num
    """
    def maxNum(self, arr, num):
        # write your code here
        def countSetBits(n):
            count = 0
            while (n):
                n &= (n-1)
                count+= 1
            return count
        ans = num
        for a in arr:
            if a % num == 0 and countSetBits(a // num) <= 1 and ans < a:
                #print(a, a //num, countSetBits(a // num))
                ans = a
            
        return num if ans == num else ans*2 

    def maxNumAC(self, arr, num):
        arr.sort()
        for n in arr:
            if n == num:
                num *= 2
        return num


if __name__ == "__main__":
     

    print(Solution().maxNum([1,2,1,3,2], 1))