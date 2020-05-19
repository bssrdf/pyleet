from UF import UF

class Solution(object):

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        return self.accountsMergeUF(accounts)
        #return self.accountsMergeDFS(accounts)

    def accountsMergeUF(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
                
        # union find
        d = {}  # key:val = email:index        
        uf = UF(len(accounts))
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in d:                   
                    uf.union(i, d[email])
                else:
                    d[email] = i
                    
        # merge accounts      
        from collections import defaultdict
        res0 = defaultdict(set)     # key:val = index: {set of emails}
        for i in range(len(accounts)):            
            res0[uf.find(i)] |= set(accounts[i][1:])
        # convert into required format
        res = []
        for k, v in res0.items():    
            res.append([accounts[k][0]] + sorted(v))
        
        return res

    def accountsMergeDFS(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i)
        # DFS code for traversing accounts.
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res



accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
            ["Mary", "mary@mail.com"]]

print(Solution().accountsMerge(accounts))



