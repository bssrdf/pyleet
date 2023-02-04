'''
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend 
all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to 
default code definition to get new method signature.
'''

import sys
class Solution(object):
    def attend(self, meetings):
        meets = sorted(meetings, key=lambda x: x[1])
        e = -sys.maxsize-1
        for m in meets:
            if m[0] < e:
                return False
            e = m[1]
        return True


print(Solution().attend([[0,30],[5,10],[15,20]]))
