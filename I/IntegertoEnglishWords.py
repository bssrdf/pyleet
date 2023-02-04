''''
-Hard-

Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 2^31 - 1

'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return LESS_THAN_20[num] + " "
            elif num < 100:
                return TENS[num // 10] + " " + helper(num % 10)
            else:
                return LESS_THAN_20[num // 100] + " Hundred " + helper(num % 100)

        if num == 0: return "Zero"
        i = 0
        words = ""
        while num > 0:
            if num % 1000 != 0:
                words = helper(num % 1000) +THOUSANDS[i] + " " + words
            num //= 1000
            i += 1
        return words.strip()



if __name__ == "__main__":
    print(Solution().numberToWords(1234567891))