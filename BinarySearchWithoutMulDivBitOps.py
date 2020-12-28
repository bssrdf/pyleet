'''
This problem was asked by Netflix.

Given a sorted list of integers of length N, determine if an element x is in the list 
without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.

'''

class Solution(object):
    def bsearch_nodiv(self, arr, n): 
        powers = [0, 1]
        next_power = powers[-1] + powers[-1] 
        while next_power < len(arr): 
            powers.append(next_power) ``
            next_power = powers[-1] + powers[-1] 
        print(powers)
        left, right, power_index = 0, len(arr) - 1, len(powers) - 1 
        while left < right: 
            while left + powers[power_index] >= len(arr): 
                power_index -= 1 
            mid = left + powers[power_index] 
            if arr[mid] == n: 
                return mid 
            if arr[mid] < n: 
                left = mid + 1 
            else: 
                right = mid 
            power_index -= 1 
        if left < len(arr) and arr[left] == n: 
            return left
        return -1

if __name__ == "__main__":
    print(Solution().bsearch_nodiv([1,3,6,8,10], 9))
    