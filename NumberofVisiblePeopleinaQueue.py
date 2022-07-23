'''
-Hard-

There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. 
You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than 
both of them. More formally, the ith person can see the jth person if i < j 
and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their 
right in the queue.

 

Example 1:



Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.
Example 2:

Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
 

Constraints:

n == heights.length
1 <= n <= 10^5
1 <= heights[i] <= 10^5
All the values of heights are unique.

Hint:
Keep popping from the stack the elements in sorted order until a value larger than arr[i] is found, 
these are the ones that person i can see.

'''

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        H = heights
        n = len(heights)
        res = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            cnt = 0
            while stack and H[stack[-1]] < H[i]:                
                cnt += 1
                stack.pop()            
            if stack: cnt += 1
            res[i] = cnt
            stack.append(i)   
        return res

        

if __name__ == "__main__":
    print(Solution().canSeePersonsCount([10,6,8,5,11,9]))
    print(Solution().canSeePersonsCount([11,19,12,15,14,18,7,1,8,9]))