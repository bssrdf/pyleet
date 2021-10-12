'''
-Medium-
*Simulation*
%Google%

Given a time represented in the format "HH:MM", form the next closest time by reusing 
the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" 
are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, 
which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. 
It may be assumed that the returned time is next day's time since it is smaller than the inpu


'''

class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here

        digits = [int(t) for t in time[:2]+time[3:]]
 #       print(digits)
        m1 = {0:9, 1:9, 2:3}
        m = {'H1': m1, 'H2': 2, 'S1': 9, 'S2': 5}
        res = []
        fail = 0
        for i,k in zip(range(3,-1,-1), ('S1','S2','H1','H2')):
            if digits[i] == (m[k][digits[0]] if k == 'H1' else m[k]): 
                res.append(digits[i])
                fail += 1
                continue 
            for j in range(digits[i]+1, (m[k][digits[0]] if k == 'H1' else m[k])+1):
                if j in digits:
                    res.append(j)
                    for l in range(i-1,-1,-1):
                        res.append(digits[l])
                    res = res[::-1]
                    return ''.join([str(i) for i in res[:2]])+":"+''.join([str(i) for i in res[2:]])

                    
         #   print(i, k, digits[i], res)
            
        if fail == 4:
            return str(min(digits))*2+':'+str(min(digits))*2            
        res = res[::-1]
        #print(res)
        return ''.join([str(i) for i in res[:2]])+":"+''.join([str(i) for i in res[2:]])

    def nextClosestTime2(self, time):
        # write your code here

        digits = [int(t) for t in time[:2]+time[3:]]
        def nextT(timeArray):
            timeArray[1] += 1
            if timeArray[1] >= 60:
                timeArray[1] %= 60
                timeArray[0] += 1
            
            if timeArray[0] >= 24:
                timeArray[0] %= 24
        def isReuse(timeArray):
            hour = timeArray[0]; minute = timeArray[1]
            if not hour // 10 in digits:
                return False
            elif not hour % 10 in digits:
                return False
            elif not minute // 10 in digits:
                return False
            elif not minute % 10 in digits:
                return False
            else:
                return True
  
        timeArray = [int(time[:2]), int(time[3:])]
        for i in range(1, 1441):
            nextT(timeArray)
            if isReuse(timeArray):
                nextTime = "{:02d}:{:02d}".format(timeArray[0], timeArray[1])
                return nextTime
        return time

if __name__ == "__main__":
    print(Solution().nextClosestTime("19:34"))
    print(Solution().nextClosestTime("23:59"))
    print(Solution().nextClosestTime("21:19"))
    print(Solution().nextClosestTime2("19:34"))
    print(Solution().nextClosestTime2("23:59"))
    print(Solution().nextClosestTime2("21:19"))