
import collections

class Solution(object):

    def dfs(self, v, level):        

        self.visited.add(v)

        if level % 2 == 0:
           self.on_the_path_even.add(v)
        else:
           self.on_the_path_odd.add(v)

        for w in self.adjList[v]:
            if w not in self.visited:
                if not self.dfs(w, level+1):
                    return False
            elif level % 2 == 0 and w in self.on_the_path_even:
                #print(f"Cycle detected: found a back edge from {v} to {w}.")
                return False
            elif level % 2 == 1 and w in self.on_the_path_odd:                
                return False
               
        if level % 2 == 0:
           self.on_the_path_even.remove(v)
        else:
           self.on_the_path_odd.remove(v)
                  
        return True

    def possisbleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
        self.adjList = collections.defaultdict(list)   
        
        for e in dislikes:
            w, v = e[0], e[1]
            self.adjList[w].append(v)
            self.adjList[v].append(w)

       
        self.visited = set()
        self.on_the_path_odd = set()
        self.on_the_path_even = set()

        for i in range(1, N+1):  
            if not self.dfs(i, 0):
                return False
        return True
    

if __name__ == "__main__":
    print(Solution().possisbleBipartition(4, [[1,2],[1,3],[2,4]]))
    print(Solution().possisbleBipartition(3, [[1,2],[1,3],[2,3]]))
    print(Solution().possisbleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
    