class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        moves={1:[8,6], 2:[7, 9], 3:[4,8],
               4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6],
               8:[1,3], 9:[2,4], 0:[4,6]}
        #dp = [[set() for _ in range(N)] for _ in range(10)]
        res = set()
        def dfs(i, n, path):
            path.append(i)                
            if n==N:               
                res.add(''.join([str(p) for p in path]))
                return
            for j in moves[i]:                
                dfs(j, n+1, path)
            path.pop()
        for i in range(10):
           dfs(i, 1, [])
        return len(res)

    def knightDialerDP(self, N):
        """
        :type N: int
        :rtype: int
        """
        moves={1:[8,6], 2:[7, 9], 3:[4,8],
               4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6],
               8:[1,3], 9:[2,4], 0:[4,6]}
        
        MOD = 10**9 + 7
        prior_case = [1] * 10                                     
        current_case = [1] * 10                                   
        current_num_hops = 1            
        while current_num_hops <= N-1:
            current_case = [0] * 10                               
            current_num_hops += 1                                 
                                                              
            for position in range(0, 10):                         
                for neighbor in moves[position]:              
                    current_case[position] += prior_case[neighbor]
                    current_case[position] %= MOD
            prior_case = current_case                             
                                                              
                
        return sum(current_case) % MOD

if __name__ == "__main__":
    N = 10
    print(Solution().knightDialer(N))
    print(Solution().knightDialerDP(N))
    

            
            
