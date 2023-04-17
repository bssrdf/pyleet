'''


'''

class DisjointSetForest:
    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        self.p[x] = y

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]


def off_line_minimum(q, n):
    pos = [-1] * (n + 1)
    m = 0
    for v in q:
        if v == 'E':
            m += 1
        else:
            pos[v] = m
    ds = DisjointSetForest(m + 1)
    extracted = [None] * m
    for i in range(1, n + 1):
        j = ds.find_set(pos[i])
        if j < m:
            extracted[j] = i
            ds.link(j, j + 1)
    return extracted

query = [4, 8, 'E', 3, 'E', 9, 2, 6, 'E', 'E', 'E', 1, 7, 'E', 5]
print(off_line_minimum(query, 9))