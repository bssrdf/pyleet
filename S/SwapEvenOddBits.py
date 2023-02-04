'''

Here’s a problem that was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd 
bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101.

Bonus: Can you do this in one line?

'''
class Solution(object):
    def swap_bits(self, x):
        # x & 0b10101010  extracts even bits
        # >> 1 then shifts them to odd positions
        # x & 0b01010101  extracts even bits    
        # << 1 then shifts them to even positions    
        # lastly | combines them together to form the final number
        return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1

if __name__ == "__main__":
    x = 0b10101010
    print("{0:8b}".format(x))
    y = Solution().swap_bits(x)
    print("{0:08b}".format(y))
    x = 0b11100010
    print("{0:8b}".format(x))
    y = Solution().swap_bits(x)
    print("{0:08b}".format(y))
