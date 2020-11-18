import bisect
import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        """
        first pointer: when you calculate cumulative sum, your array is sorted and you 
        can do a binary search.
        example:
        input: [3, 1, 4, 2]
        cum sum: [3, 4, 8, 10]
        now, just get random element in range (0, 10(last element of cum sum)).
        now, when you search for that random element in cum sum then you are 
        actually doing weighted picking! Think about it.
        """
        
        self.list = w      
        self.total = 0
        self.cum_weights = []
        for w in self.list:
            self.total += w
            self.cum_weights.append(self.total)

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(0, self.total-1)
        i = bisect.bisect(self.cum_weights, x)
        return i        
    
if __name__=="__main__":
    #obj = Solution([3,14,1,7])
    obj = Solution([1])
    for i in range(100):
        print(obj.pickIndex())
        