'''
-Medium-

On a table are N cards, with a positive integer printed on the front and back of 
each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number X on the back of the chosen card is not on the front of any card, 
then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of 
card i. 

A flip swaps the front and back numbers, so the value on the front is now on 
the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the 
backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on 
the front of any card, so 2 is good. 

Note:

1 <= fronts.length == backs.length <= 1000.
1 <= fronts[i] <= 2000.
1 <= backs[i] <= 2000.

More clear problem statement:

There are N numbers in fronts, N numbers in backs.
X is a 'good number' if it satisfies both of the following requirements:
1. there does NOT exist an index i in [0, N-1] such that fronts[i] == backs[i] == X.
In other words, X can't appear on both the front and back sides of any (same) card.
2. X is a number from either fronts or backs.

Find the smallest good number.

'''

class Solution(object):
    

    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        S = set()
        res = 2001
        for f,b in zip(fronts, backs):
            if f == b:
               S.add(f)
        for i in fronts+backs:                        
            if i not in S:
               res = min(res, i)            
        return 0 if res == 2001 else res
            

if __name__ == "__main__":
    print(Solution().flipgame([1,2,4,4,7], [1,3,4,1,3]))
    print(Solution().flipgame([1,1], [1,2]))