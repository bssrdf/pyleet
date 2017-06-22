'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        nums = [1] *len(ratings)
        c = 1
        csum = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                c += 1
                if nums[i] < c:   
                    nums[i] = c
            else:
                c = 1
        print 'phase 1 ', nums
        c = 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                c += 1
                if nums[i] < c:    
                    nums[i] = c
            else:
                c = 1
        print 'phase 2 ', nums
        for i in nums:
            csum += i
        return csum

if __name__ == "__main__":
    #assert Solution().candy([1, 2, 3, 7, 4, 3, 2, 1]) == 21
    #candies = [1, 2, 3, 7, 4, 3, 2, 1]
    candies = [1, 2, 3, 7, 5, 7, 4, 3, 2, 1]
    print '        ',  candies
    print Solution().candy(candies)
