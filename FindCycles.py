import collections

class Solution(object):

    def dfs(self, v):
        #if self.visited[v]:
        #    return True
            
        #self.visited[v] = True
        #self.on_the_path[v] = True

        self.visited.add(v)
        self.on_the_path.add(v)

        for w in self.adjList[v]:
            if w not in self.visited:
                if self.dfs(w):
                    return True
            elif w in self.on_the_path:
                print(f"Cycle detected: found a back edge from {v} to {w}.")
                return True
            #if not self.visited[w]:
            #    if self.dfs(w):
            #        return True
            #elif self.on_the_path[w]:
            #     return True
        #self.on_the_path[v] = False       
        self.on_the_path.remove(v)
                  
        return False



    def detectCycles(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: Bool
        """
    
        n = len(edges)
        #self.adjList = [[] for i in range(n+1)]    
        self.adjList = collections.defaultdict(list)   

        
        for e in edges:
            w, v = e[0], e[1]
            self.adjList[w].append(v)
            
        #self.visited = [False] * (n+1)
        #self.on_the_path = [False] * (n+1)
        self.visited = set()
        self.on_the_path = set()

        return self.dfs(edges[0][0])
        


print(Solution().detectCycles([[1,2], [2,3], [3,4], [4,1], [1,5]]))
print(Solution().detectCycles([[1,2], [1,3], [2,3]]))
print(Solution().detectCycles([[2,1],[3,1],[4,2],[1,4]]))
print(Solution().detectCycles([('u', 'v'),
        ('u', 'x'),
        ('v', 'y'),
        ('w', 'y'),
        ('w', 'z'),
        ('x', 'v'),
        ('y', 'x')]))




#import collections


class Graph(object):
    def __init__(self, edges):
        self.edges = edges
        self.adj = Graph._build_adjacency_list(edges)

    @staticmethod
    def _build_adjacency_list(edges):
        adj = collections.defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
        return adj


def dfs(G):
    discovered = set()
    finished = set()

    for u in G.adj:
        if u not in discovered and u not in finished:
            discovered, finished = dfs_visit(G, u, discovered, finished)


def dfs_visit(G, u, discovered, finished):
    discovered.add(u)
    finished.add(u)
    for v in G.adj[u]:
        # Detect cycles
        if v in discovered:
            print(f"Cycle detected: found a back edge from {u} to {v}.")
            #return discovered, finished
        # Recurse into DFS tree
        if v not in finished:
            dfs_visit(G, v, discovered, finished)

    discovered.remove(u)
    

    return discovered, finished


if __name__ == "__main__":
    G = Graph([
        ('u', 'v'),
        ('u', 'x'),
        ('v', 'y'),
        ('w', 'y'),
        ('w', 'z'),
        ('x', 'v'),
        ('y', 'x'),
        ('z', 'z')])

    dfs(G)
