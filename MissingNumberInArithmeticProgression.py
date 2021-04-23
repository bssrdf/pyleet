'''
-Easy-

Given an array that represents elements of arithmetic progression in order. One element 
is missing in the progression, find the missing number.
Examples:


Input: arr[]  = {2, 4, 8, 10, 12, 14}
Output: 6

Input: arr[]  = {1, 6, 11, 16, 21, 31};
Output: 26

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5

'''
class Soluion(object):
    def missingNumber(self, arr):
        diff1 = arr[-1] - arr[-2]
        diff2 = arr[1] - arr[0]
        if diff1 == 2 * diff2: return arr[-2]+diff2
        elif diff2 == 2 * diff1: return arr[0]+diff1
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != diff1:
                return arr[i] + diff1
        return arr[0]

if __name__ == "__main__":
    print(Soluion().missingNumber([2, 4, 8, 10, 12, 14]))
    print(Soluion().missingNumber([1, 6, 11, 16, 21, 31]))
    print(Soluion().missingNumber([5,7,11,13]))