
from collections import defaultdict


n = 9; edges = [[2,5],[3,4],[4,1],[1,7],[6,7],[7,0],[0,5],[5,8]]    
# n = 4; edges = [[0,1],[1,2],[1,3]]
# n = 5; edges = [[2,0],[3,1],[1,0],[0,4]]

f = [[0]*22 for _ in range(n+1)]
# if node start 1
dep = [-1]*(n+1)
G = defaultdict(list)

for u,v in edges:
    # if node index starts at 0
    G[u+1].append(v+1)
    G[v+1].append(u+1)
    # else
    # G[u].append(v)
    # G[v].append(u)

def dfs(u, pre):
    f[u][0] = pre
    dep[u] = dep[pre] + 1
    for i in range(1, 22):
        f[u][i] = f[f[u][i - 1]][i - 1]
        # if dep[u] - (1 << i) >= 1: break

    for v in G[u]:
        if v == pre: continue
        dfs(v, u)

def lca(x, y):
    if dep[x] > dep[y]:
        x, y = y, x
    # for i in range(21, -1, -1):
    #     if dep[f[y][i]] >= dep[x]: y = f[y][i]
    tmp = dep[y] - dep[x]
    for j in range(22): 
        if tmp == 0: break
        if tmp & 1: y = f[y][j]
        tmp >>= 1     
    if x == y: return x
    for i in range(21, -1, -1):
        if f[x][i] != f[y][i]:
            x = f[x][i]
            y = f[y][i]
    return f[x][0]

dfs(1, 0)
# for i in range(n):
#     print(i, f[i][0])
# print(dep)
x, y = 3, 6
print('x = ', x, 'y = ', y, 'lca(x,y) = ', lca(x+1,y+1)-1)
x, y = 4, 8
print('x = ', x, 'y = ', y, 'lca(x,y) = ', lca(x+1,y+1)-1)
x, y = 3, 2
print('x = ', x, 'y = ', y, 'lca(x,y) = ', lca(x+1,y+1)-1)
x, y = 0, 6
print('x = ', x, 'y = ', y, 'lca(x,y) = ', lca(x+1,y+1)-1)
x, y = 0, 2
print('x = ', x, 'y = ', y, 'lca(x,y) = ', lca(x+1,y+1)-1)

x, y = 4, 3
print('x = ', x, 'y = ', y, 'lca(x,y) = ', lca(x+1,y+1)-1)