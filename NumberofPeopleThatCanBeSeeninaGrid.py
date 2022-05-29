'''


You are given an m x n 0-indexed 2D array of positive integers heights where heights[i][j] is the height of the person standing at position (i, j).

A person standing at position (row1, col1) can see a person standing at position (row2, col2) if:

The person at (row2, col2) is to the right or below the person at (row1, col1). More formally, this means that either row1 == row2 and col1 < col2 or row1 < row2 and col1 == col2.
Everyone in between them is shorter than both of them.
Return an m x n 2D array of integers answer where answer[i][j] is the number of people that the person at position (i, j) can see.

 

Example 1:



Input: heights = [[3,1,4,2,5]]
Output: [[2,1,2,1,0]]
Explanation:
- The person at (0, 0) can see the people at (0, 1) and (0, 2).
  Note that he cannot see the person at (0, 4) because the person at (0, 2) is taller than him.
- The person at (0, 1) can see the person at (0, 2).
- The person at (0, 2) can see the people at (0, 3) and (0, 4).
- The person at (0, 3) can see the person at (0, 4).
- The person at (0, 4) cannot see anybody.
Example 2:



Input: heights = [[5,1],[3,1],[4,1]]
Output: [[3,1],[2,1],[1,0]]
Explanation:
- The person at (0, 0) can see the people at (0, 1), (1, 0) and (2, 0).
- The person at (0, 1) can see the person at (1, 1).
- The person at (1, 0) can see the people at (1, 1) and (2, 0).
- The person at (1, 1) can see the person at (2, 1).
- The person at (2, 0) can see the person at (2, 1).
- The person at (2, 1) cannot see anybody.
 

Constraints:

1 <= heights.length <= 400
1 <= heights[i].length <= 400
1 <= heights[i][j] <= 105

'''



class Solution:
    def canBeSee(self, heights):
        H = heights
        m, n = map(len, (H, H[0]))
        nextGreaterRow = [[n-1]*n for _ in range(m)]
        nextGreaterCol = [[m-1]*n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            stack = []
            for j in range(n):
                while stack and H[i][stack[-1]] <= H[i][j]:
                    nextGreaterRow[i][stack.pop()] = j
                stack.append(j)
        for j in range(n):
            stack = []
            for i in range(m): 
                while stack and H[stack[-1]][j] <= H[i][j]:
                    nextGreaterCol[stack.pop()][j] = i
                stack.append(i)
        # print(m, n)
        # print(nextGreaterRow)
        for i in range(m):
            for j in range(n):
                ans[i][j] = (nextGreaterRow[i][j]-j) + (nextGreaterCol[i][j]-i)
        return ans 

    def canBeSee2(self, heights):
        H = heights
        m, n = map(len, (H, H[0]))
        nextGreaterCol = [[m-1]*n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]        
        for j in range(n):
            stack = []            
            for i in range(m): 
                while stack and H[stack[-1]][j] <= H[i][j]:
                    nextGreaterCol[stack.pop()][j] = i
                stack.append(i)
        # print(m, n)
        # print(nextGreaterRow)
        for i in range(m):
            stack = []
            nextGreaterRow = [n-1]*n
            for j in range(n):
                while stack and H[i][stack[-1]] <= H[i][j]:
                    nextGreaterRow[stack.pop()] = j                    
                stack.append(j)
            for j in range(n):
                ans[i][j] = (nextGreaterRow[j]-j) + (nextGreaterCol[i][j]-i)
        return ans 
        

if __name__ == "__main__":
    heights = [[3,1,4,2,5]]
    print(Solution().canBeSee(heights))
    heights = [[5,1],[3,1],[4,1]]
    print(Solution().canBeSee(heights))

    heights = [[3,1,4,2,5]]
    print(Solution().canBeSee2(heights))
    heights = [[5,1],[3,1],[4,1]]
    print(Solution().canBeSee2(heights))