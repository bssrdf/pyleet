'''

-Medium-
*Bit*

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following 
rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, 
followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a 
valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each 
integer is used to store the data. This means each integer represents only 
1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 
00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte 
character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 
10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

'''

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        mask4  = 0b00001111
        mask3  = 0b00000111
        mask2  = 0b00000011
        mask1  = 0b00000000
        mask10 = 0b00000010        
        n = len(data)
        i = 0
        conbytes = 0        
        while i < n:        
            if mask1 | data[i]>>7 == mask1: 
                i += 1
                continue
            match = False            
            if mask4 & data[i]>>4 == mask4 \
               and (0b1<<3) & data[i] == 0:               
                match = True
                conbytes = 3
            elif mask3 & data[i]>>5 == mask3 \
                and (0b1<<4) & data[i] == 0:                            
                match = True
                conbytes = 2
            elif mask2 & data[i]>>6 == mask2 \
                and (0b1<<5) & data[i] == 0:                                         
                match = True
                conbytes = 1
            if not match:
                return False
            if i+conbytes > n-1: return False
            j = i+1
            while j <= i+conbytes:
                if mask10 & data[j]>>6 != mask10:
                    return False
                j += 1
            i = j            
        return True

if __name__ == "__main__":
    print(Solution().validUtf8([197, 130, 1]))
    print(Solution().validUtf8([235, 140, 4]))
    print(Solution().validUtf8([240,162,138,147,145]))
    print(Solution().validUtf8([248,130,130,130]))