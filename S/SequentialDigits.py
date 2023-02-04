'''
An integer has sequential digits if and only if each digit in the number is one more 
than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have 
sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

'''

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        l, h = low, high
        m, n = 0, 0
        while l:
            m += 1
            l //= 10
        while h:
            n += 1
            h //= 10            
        ans = []
        digits = '123456789'
        for k in range(m,n+1):
            for i in range(0, len(digits)-k+1):
                num = int(digits[i:i+k])
                if low <= num <= high:
                    ans.append(num)            
           
        return ans        

if __name__ == "__main__":
    print(Solution().sequentialDigits(1000, 13000))