'''
-Hard-
*DP*
*Memoization*
*Bitmask*
*Bipartite*
Given a m * n matrix seats  that represent seats distributions in a classroom. 
If a seat is broken, it is denoted by '#' character otherwise it is denoted 
by a '.' character.

Students can see the answers of those sitting next to the left, right, upper 
left and upper right, but he cannot see the answers of the student sitting 
directly in front or behind him. Return the maximum number of students that 
can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

'''
from functools import lru_cache
class Solution(object):

    def maxStudents(self, seats):
        R, C = len(seats), len(seats[0])
        
        matching = [[-1] * C for _ in range(R)]
        
        def dfs(node, seen):
            r, c = node
            # assume a virtual edge connecting students who can spy
            for nr, nc in [[r-1,c-1], [r,c-1],[r,c+1],[r-1,c+1],[r+1,c-1],[r+1,c+1]]: 
                if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc] and seats[nr][nc] == '.':
                    seen[nr][nc] = True
                    if matching[nr][nc] == -1 or dfs(matching[nr][nc], seen):
                        #if nr == 2 and nc == 1: 
                        #    print('r,c:', r, c) 
                        matching[nr][nc] = (r,c)
                      #  matching[r][c] = (nr,nc)
                        return True
            return False
        
        def Hungarian():
            res = 0
            for c in range(0,C,2):
                for r in range(R):
                    if seats[r][c] == '.':
                        seen = [[False] * C for _ in range(R)]
                        if dfs((r,c), seen):
                            res += 1            
            return res
        
        res = Hungarian()
        for r in range(R):
            print(matching[r])        
                
        count = 0
        for r in range(R):
            for c in range(C):
                if seats[r][c] == '.':
                    count += 1
        for row in range(R):
            for col in range(C):
                if seats[row][col] == '.' and matching[row][col] == -1:
                    seats[row][col] = 'X'
        for r in range(R):
            print(seats[r])                    
        return count - res


    '''

    a brute force solution is to place some students row by row without violating rules,
    count their # and update our target maximum

    a better solution is to use DP with memoization (lru_cache in python).    

    '''    
    
    def maxStudentsBitMask(self, seats):
        @lru_cache(None)
        def backtracking(row: int, prev: int):
            if row == m: return 0
            mask, max_student = bitmasks[row], 0
            '''
                We can use (x >> i) & 1 to get i-th bit in state x, where >> is the right 
                shift operation. If we are doing this in an if statement (i.e. to check 
                whether the i-th bit is 1), we can also use x & (1 << i), where the << 
                is the left shift operation.

                We can use (x & y) == x to check if x is a subset of y. The subset means 
                every state in x could be 1 only if the corresponding state in y is 1.

                We can use (x & (x >> 1)) == 0 to check if there are no adjancent valid 
                states in x.

                We can use a bitmask of n bits to represent the validity of each row in 
                the classroom. The i-th bit is 1 if and only if the i-th seat is not 
                broken. For the first example in this problem, the bitmasks will be 
                "010010", "100001" and "010010". When we arrange the students to seat 
                in this row, we can also use n bits to represent the students. The i-th 
                bit is 1 if and only if the i-th seat is occupied by a student. We should 
                notice that n bits representing students must be a subset of n bits 
                representing seats.
            '''
            # the loop below iterates every bit pattern for #'s between 0 and (1<<n)-1
            for bits in range(1 << n):                
                '''
                 using the conditionals below, only valid placement of students get picked
                 on the current row; 
                 (mask & bits) == bits: each student occupies a valid(unbroken) seat
                 not (bits & (bits >> 1)): no two students seats adjacent
                 (prev & (bits << 1)): the seat to the left and on the row above not occupied
                 (prev & (bits >> 1)): the seat to the right and on the row above not occupied
                '''
                if (mask & bits) == bits and not (bits & (bits >> 1)):
                    if not (prev & (bits >> 1)) and not (prev & (bits << 1)):
                        students = bin(bits).count('1')
                        '''
                        move to next row by recursion to get maximum students for all rows
                        below
                        '''
                        rest_students = backtracking(row + 1, bits)
                        # combining # of students on the current row and from all rows
                        # below, we can update max which is what we need
                        max_student = max(max_student, students + rest_students)
                        #print(row, students, format(bits, '05b'), rest_students, max_student)
            return max_student

        m, n = len(seats), len(seats[0])
        bitmasks = []
        for row in seats:
            bits = ('1' if seat == '.' else '0' for seat in row)
            bitmasks.append(int(''.join(bits), 2))
        #for row in bitmasks:
        #    print(format(row,'0'+str(n)+'b'))
        return backtracking(0, 0) 


if __name__ == "__main__":
    #'''
    seats =    [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
    '''
    #seats = [["#",".","#","#",".","#"],
             [".","#","#","#","#","."],
             ["#",".","#","#",".","#"]]
    '''
    print(Solution().maxStudents(seats))
    #print(Solution().maxStudentsBitMask(seats))