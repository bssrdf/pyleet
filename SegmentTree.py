class Node:
    def __init__(self, left_side, right_side):
        self.val = None
        self.ls, self.rs = left_side, right_side
        self.left_child, self.right_child = None, None


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.vals = arr[:]
        self.root = self.build(0, self.n)

    def build(self, l, r):
        # 传入的l和r表示区间范围，左闭右开
        if r - l < 1:
            return None
        node = Node(l, r)
        # 如果区间长度是1，说明是叶子节点了，直接将val赋值成对应的数值
        if r - l == 1:
            node.val = self.vals[l]
        else:
            # 否则递归调用
            m = (l + r) >> 1
            node.left_child = self.build(l, m)
            node.right_child = self.build(m, r)
            node.val = min(node.left_child.val, node.right_child.val)
        return node
    
    def update(self, k, v):
        self._update(self.root, k, v)

    def _update(self, u, k, v):
        if u is None:
            return
        # 如果k在u这个节点维护的区间里
        if u.ls <= k < u.rs:
            # 更新它的最小值
            u.val = min(u.val, v)
            m = (u.ls + u.rs) >> 1
            # 判断往左还是往右
            if k < m:
                self._update(u.left_child, k, v)
            else:
                self._update(u.right_child, k, v)
    
    def query(self, l, r):
        return self._query(self.root, l, r)

    def _query(self, u, l, r):
        # l和r是查询区间
        # 如果查询区间是u节点区间的超集
        if l <= u.ls and r >= u.rs:
            return u.val
        # 如果查询区间只和u节点区间的左半部分有交集
        elif r <= u.left_child.rs:
            return self._query(u.left_child, l, r)
        # 如果查询区间只和u节点右半部分有交集
        elif l >= u.right_child.ls:
            return self._query(u.right_child, l, r)
        # 如果都有交集
        return min(self._query(u.left_child, l, r), self._query(u.right_child, l, r))