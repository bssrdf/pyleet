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

        Can you perform a breadth-first traversal instead, where you start at the top 
        and “visit” function calls for N-1 hops only after you’ve visited those for N 
        hops? Sadly, no. The values of function calls with nonzero hops absolutely 
        require the values from smaller hop counts, so you won’t get any results until 
        you reach the zero-hop layer and start returning numbers rather than additional 
        function calls (note the zero-hop layer isn’t depicted here).

        You can however, reverse the order: visit layers with N hops only after you’ve 
        visited layers with N-1 hops. Those of you who studied or are studying discrete 
        mathematics will recognize all the necessary ingredients for an induction: we know 
        that the values of zero-hop function calls are always one (the base case). We also 
        know how to combine N-1 hop values to get N hop values, using the recurrence relation 
        (the inductive step). We can start with a base case of zero hops and induce all values 
        greater than zero.

        """
        moves={1:[8,6], 2:[7, 9], 3:[4,8],
               4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6],
               8:[1,3], 9:[2,4], 0:[4,6]}
        
        MOD = 10**9 + 7
        # base case: N=1, 1 hop should generate 1 number for each dial 
        prior_case = [1] * 10                                     
        current_case = [0] * 10                                   
        current_num_hops = 1            
        while current_num_hops <= N-1:
            current_case = [0] * 10                               
            current_num_hops += 1                                 
            # induction: we know the number of generated numbers for n-1 hops T_i(n-1)
            # the the number of generated numbers for n hops T_i(n) = sum(T_i_p(n-1)) 
            # over all neighbors p of digit i                                                  
            for position in range(0, 10):                         
                for neighbor in moves[position]:              
                    current_case[position] += prior_case[neighbor]
                    current_case[position] %= MOD
            prior_case = current_case                             
                                                              
                
        return sum(prior_case) % MOD

if __name__ == "__main__":
    N = 10
    print(Solution().knightDialer(N))
    print(Solution().knightDialerDP(N))
    

            
            
